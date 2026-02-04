from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from rest_framework import status


class ChildActivityResponseRawAPI(APIView):

    def post(self, request):
        child_id = request.data.get("child_id")
        activity_id = request.data.get("activity_id")

        if not child_id or not activity_id:
            return Response(
                {"error": "child_id and activity_id required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        with connection.cursor() as cursor:

           
            cursor.execute("""
                SELECT si_no, is_completed
                FROM child_dloat_skill_assessment
                WHERE child_id = %s
                ORDER BY si_no DESC
                LIMIT 1
            """, [child_id])

            assessment = cursor.fetchone()
            if not assessment:
                return Response({"error": "Assessment not found"}, status=404)

            si_no, completion_status = assessment

          
            cursor.execute("""
                SELECT
                    q.question_id,
                    q.question_txt,
                    q.correct_answer,
                    cdr.given_ans_text,
                    cdr.analysis
                FROM child_dloat_responses cdr
                JOIN dloat_questions q
                    ON q.question_id = cdr.question_id
                WHERE cdr.child_assessment_id = %s
                  AND q.class_skill_id = %s
            """, [si_no, activity_id])

            rows = cursor.fetchall()

            responses = []
            correct = 0

            for r in rows:
                if r[4] == 1:
                    correct += 1

                responses.append({
                    "question_id": r[0],
                    "question_text": r[1],
                    "expected_ans": r[2],
                    "given_ans": r[3],
                    "analysis": r[4]
                })

            total = len(responses)
            score = (correct / total) * 100 if total else 0

          
            cursor.execute("""
                SELECT
                    status_label,
                    inference_template,
                    recommendation_template
                FROM dloat_scoring_norms
                WHERE activity_id = %s
                  AND %s BETWEEN min_score AND max_score
                LIMIT 1
            """, [activity_id, score])

            inference_row = cursor.fetchone()

        inference = None
        if inference_row:
            inference = {
                "status_label": inference_row[0],
                "inference_template": inference_row[1],
                "recommendation_template": inference_row[2]
            }

        return Response({
            "activity_id": activity_id,
            "completion_status": completion_status,
            "responses": responses,
            "inference": inference
        })
