# from django.db import models

# from django.db import models


# class ChildDloatSkillAssessment(models.Model):
#     si_no = models.AutoField(primary_key=True)

#     child_skill_map_id = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     child_id = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     enabler_id = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     is_completed = models.BooleanField(
#         default=False
#     )

#     is_stopped = models.BooleanField(
#         null=True,
#         blank=True
#     )

#     is_valid = models.BooleanField(
#         default=False
#     )

#     remarks = models.TextField(
#         null=True,
#         blank=True
#     )

#     child_final_grade = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     created_by = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     created_on = models.DateTimeField(
#         auto_now_add=True
#     )

#     updated_on = models.DateTimeField(
#         null=True,
#         blank=True
#     )

#     class Meta:
#         db_table = "child_dloat_skill_assessment"
#         managed = False   

#     def __str__(self):
#         return f"Assessment {self.si_no} | Child {self.child_id}"

    
    
 

# class ChildDloatResponses(models.Model):
#     si_no = models.AutoField(primary_key=True)

#     child_assessment = models.ForeignKey(
#         'ChildDloatSkillAssessment',
#         db_column='child_assessment_id',
#         on_delete=models.CASCADE
#     )

#     question_id = models.IntegerField()
#     given_ans_id = models.IntegerField(null=True, blank=True)
#     given_ans_text = models.CharField(max_length=255, null=True, blank=True)

#     analysis = models.BooleanField(default=False)
#     remarks = models.TextField(null=True, blank=True)

#     created_by = models.IntegerField()
#     created_on = models.DateTimeField()

#     class Meta:
#         db_table = 'child_dloat_responses'
#         managed = False

#     def __str__(self):
#         return f"Assessment {self.child_assessment_id} | Q{self.question_id}"
    
    
    
   
# class ThreeRlabsChild(models.Model):
#     child_company = models.ForeignKey(
#         ThreeRlabsCompany, on_delete=models.RESTRICT)
#     child_id = models.AutoField(primary_key=True)
#     child_view_id = models.CharField(max_length=12, blank=True, null=True)
#     child_class_id = models.ForeignKey(
#         ThreeRlabsClass, db_column="child_class_id", on_delete=models.RESTRICT
#     )
#     child_name = models.CharField(max_length=100)
#     child_parent = models.ForeignKey(
#         ThreeRlabsUsers, db_column="child_parent_id", on_delete=models.RESTRICT
#     )
#     child_enabler_id = models.IntegerField(blank=True, null=True)
#     child_original_grade = models.IntegerField(blank=True, null=True)
#     child_updated_grade = models.IntegerField(blank=True, null=True)
#     child_gender = models.ForeignKey(
#         ThreeRlabsMeta, db_column="child_gender", on_delete=models.RESTRICT
#     )
#     child_school_id = models.ForeignKey(
#         ThreeRlabsSchool, db_column="child_school_id", on_delete=models.RESTRICT
#     )
#     child_school_name = models.CharField(max_length=100, blank=True, null=True)
#     child_school_board = models.ForeignKey(
#         ThreeRLabsChildBoardList,
#         db_column="child_school_board",
#         on_delete=models.RESTRICT,
#     # )
#     child_class_standard = models.IntegerField(blank=True, null=True)
#     # child_dob = models.DateField(blank=True, null=True)
#     child_teacher_eval_completed = models.CharField(max_length=1, default="N")
#     child_teacher_eval_result = models.CharField(
#         max_length=1, blank=True, null=True)
#     child_parent_eval_required = models.CharField(max_length=1, default="N")
#     child_parent_eval_completed = models.CharField(max_length=1, default="N")
#     # child_parent_eval_result = models.CharField(
#         max_length=1, blank=True, null=True)
#     child_parent_eval_agree = models.CharField(max_length=1, default="N")
#     child_level1_eval_required = models.CharField(
#         max_length=1, blank=True, null=True)
#     child_level1_completed = models.CharField(max_length=1, default="N")
#     child_level1_result = models.CharField(max_length=1, blank=True, null=True)
#     child_eval_meeting_slot1 = models.DateTimeField(blank=True, null=True)
#     child_eval_meeting_slot2 = models.DateTimeField(blank=True, null=True)
#     child_eval_meeting_slot3 = models.DateTimeField(blank=True, null=True)
#     child_eval_confirmed_slot = models.DateTimeField(blank=True, null=True)
#     child_eval_meeting_link = models.CharField(
#         max_length=200, blank=True, null=True)
#     child_assessment_report = models.FileField(
#         blank=True, null=True, upload_to="")
#     child_level_2_enabler_id = models.ForeignKey(
#         ThreeRlabsUsers,
#         db_column="child_level_2_enabler_id",
#         related_name="child_level_2_enabler_id",
#         on_delete=models.CASCADE,
#     )
#     child_level2_completed = models.CharField(
#         max_length=1, blank=True, null=True)
#     level_1_completed_on = models.DateTimeField(blank=True, null=True)
#     level_2_completed_on = models.DateTimeField(blank=True, null=True)
#     child_level2_result = models.CharField(max_length=1, blank=True, null=True)
#     child_level2_risk = models.CharField(max_length=1, blank=True, null=True)
#     child_level2_report_upload = models.CharField(
#         max_length=200, blank=True, null=True)
#     child_level2_video_uploaded = models.CharField(
#         db_column="child_Level2_video_uploaded", max_length=1, blank=True, null=True
#     )  # Field name made lowercase.
#     child_remedial_course_required = models.CharField(
#         max_length=1, blank=True, null=True
#     )
#     child_remedial_course_enrolled = models.CharField(
#         max_length=1, blank=True, null=True
#     )
#     child_remarks = models.CharField(max_length=500, blank=True, null=True)
#     child_parent_invite = models.TextField(
#         blank=True, null=True
#     )  # This field type is a guess.
#     child_parent_reminder = models.TextField(
#         blank=True, null=True
#     )  # This field type is a guess.
#     child_valid = models.BooleanField()  # This field type is a guess.
#     child_created_by = models.IntegerField(blank=True, null=True)
#     child_assessed = models.IntegerField(blank=True, null=True)
#     no_of_reschedules_pending = models.IntegerField(blank=True, null=True)
#     no_of_classes_pending = models.IntegerField(blank=True, null=True)
#     child_assessment_device = models.CharField(
#         # max_length=30, blank=True, null=True)
#     child_internet_connectivity = models.CharField(
#         max_length=30, blank=True, null=True)
#     child_created_on = models.DateTimeField(blank=True, null=True)
#     child_modified_by = models.IntegerField(blank=True, null=True)
#     child_modified_on = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = "3rlabs_child"
#         unique_together = (("child_name", "child_parent", "child_gender"),)

#     def get_child_id(self, child_view_id):
#         return self.child_id

# class DloatAssessmentParts(models.Model):
#     id = models.AutoField(primary_key=True)

#     name = models.CharField(
#         max_length=100,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     sequence_order = models.IntegerField()

#     class Meta:
#         db_table = 'dloat_assessment_parts'
#         managed = False

#     def __str__(self):
#         return f"{self.name} ({self.sequence_order})"


# class DloatAssessmentDomains(models.Model):
#     id = models.AutoField(primary_key=True)

#     part_id = models.IntegerField()  
   

#     name = models.CharField(
#         max_length=100,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     description = models.TextField(
#         null=True,
#         blank=True,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     sequence_order = models.IntegerField()

#     class Meta:
#         db_table = 'dloat_assessment_domains'
#         managed = False

#     def __str__(self):
#         return f"{self.name} (Part {self.part_id})"



# class DloatAssessmentSkills(models.Model):
#     id = models.AutoField(primary_key=True)

#     domain_id = models.IntegerField()
 

#     name = models.CharField(
#         max_length=150,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     slug = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True,
#         unique=True,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     class Meta:
#         db_table = 'dloat_assessment_skills'
#         managed = False

#     def __str__(self):
#         return self.name
    
    
#     from django.db import models

# class DloatAssessmentActivities(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     skill_id = models.IntegerField()


#     question_view = models.CharField(
#         max_length=10,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     flow_order = models.IntegerField()
#     target_class_level = models.IntegerField()

#     name = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     max_questions = models.IntegerField(default=5)

#     is_mandatory_all = models.BooleanField(default=False)

#     is_options = models.IntegerField(null=True, blank=True)

#     class_move_to = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         db_collation='utf8mb4_unicode_ci'
#     )

#     is_inference_required = models.BooleanField(default=False)
#     is_manual_validation = models.BooleanField()
#     is_automated_inference = models.BooleanField()
#     show_writing_note = models.BooleanField(default=False)

#     instruction_id = models.IntegerField(null=True, blank=True)
    

#     class Meta:
#         db_table = 'dloat_assessment_activities'
#         managed = False

#     def __str__(self):
#         return f"Activity {self.id} (Skill {self.skill_id})"




# class DloatQuestions(models.Model):
#     question_id = models.AutoField(primary_key=True)

#     current_question = models.IntegerField(null=True, blank=True)
#     class_skill_id = models.BigIntegerField()
#     screen_type = models.CharField(max_length=50)

#     instruction = models.TextField(null=True, blank=True)
#     question_txt = models.TextField(null=True, blank=True)
#     sub_question = models.TextField(null=True, blank=True)

#     audio_url = models.CharField(max_length=255, null=True, blank=True)
#     image_url = models.CharField(max_length=255, null=True, blank=True)

#     is_manual_validation = models.BooleanField(default=False)

#     question_metadata = models.JSONField(null=True, blank=True)

#     question_type_choices = [
#         ('MCQ', 'MCQ'),
#         ('INPUT', 'INPUT'),
#         ('MIXED', 'MIXED'),
#     ]
#     question_type = models.CharField(
#         max_length=10,
#         choices=question_type_choices
#     )

#     correct_answer = models.TextField(null=True, blank=True)

#     show_question = models.BooleanField(default=True)
#     show_options = models.BooleanField(default=True)

#     stream_audio_url = models.CharField(max_length=255, null=True, blank=True)
#     stream_audio_status = models.CharField(max_length=50, null=True, blank=True)

#     class Meta:
#         db_table = 'dloat_questions'
#         managed = False

#     def __str__(self):
#         return f"Question {self.question_id} - {self.screen_type}"



# class DloatChildInferences(models.Model):
#     inference_id = models.BigAutoField(primary_key=True)

#     child_id = models.IntegerField()
#     class_skill_id = models.IntegerField()
#     assessment_session_id = models.IntegerField()
#     scoring_norm_id = models.IntegerField()

#     score_percentage = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         null=True,
#         blank=True
#     )

#     inference_text = models.TextField()

#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'dloat_child_inferences'
#         managed = False

#     def __str__(self):
#         return f"Inference {self.inference_id} | Child {self.child_id}"
    
    




# class DloatScoringNorm(models.Model):
#     id = models.AutoField(primary_key=True)

#     activity_id = models.BigIntegerField()

#     min_score = models.IntegerField()
#     max_score = models.IntegerField()

#     status_label = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True
#     )

#     inference_order = models.IntegerField(
#         null=True,
#         blank=True
#     )

#     inference_type = models.CharField(
#         max_length=10,
#         null=True,
#         blank=True
#     )

#     inference_template = models.TextField(
#         null=True,
#         blank=True
#     )

#     recommendation_template = models.TextField(
#         null=True,
#         blank=True
#     )

#     class Meta:
#         db_table = "dloat_scoring_norms"
#         managed = False   

#     def __str__(self):
#         return f"Norm {self.id} | Activity {self.activity_id}"
