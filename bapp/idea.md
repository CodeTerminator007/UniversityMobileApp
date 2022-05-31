#  query to get total lectures
Attendance.objects.all().values('class_id', 'subject_id__subject_name', 'subject_id__staff_id__username').annotate(total_lectures=Count('id'))


# total absents and presents
AttendanceReport.objects.filter(student_id=Student.objects.last()).values(
    CourseName=F('subject_id__subject_name'),
    TeacherName=F('subject_id__staff_id__username')
     ).annotate(total_present=Count(
         Case(
             When(
                status=True,
                then=1
         ))),
         total_absent=Count(Case(When(status=False,then=1)))
         )



# Values k custom name

    Attendance.objects.all().values('class_id', CourseName=F('subject_id__subject_name'), TeacherName=F('subject_id__staff_id__username')).annotate(total_lectures=Count('id'))


total_data = Attendance.objects.all().values('class_id', 'subject_id__subject_name', 'subject_id__staff_id__username').annotate(total_lectures=Count('id'))
report_data = AttendanceReport.objects.filter(student_id=Student.objects.last()).values(
    CourseName=F('subject_id__subject_name'),
    TeacherName=F('subject_id__staff_id__username')
     ).annotate(total_present=Count(
         Case(
             When(
                status=True,
                then=1
         ))),
         total_absent=Count(Case(When(status=False,then=1)))
         )

subject_total_lecure_map =  {}

for x in total_data:
    subject_total_lecure_map[x['subject_id__subject_name']] = x['total_lectures']

for x in report_data:
    x['Lectures']=subject_total_lecure_map[x['CourseName']]
    x['Percentage'] =  10 #percentage calculate kro