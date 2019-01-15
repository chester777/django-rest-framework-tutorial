from django.db import models


class Instructor(models.Model):
    '''
    Django 의 models.Model 을 상속받아 모델을 정의 할 경우, pk 를 자동으로 생성해준다.
    이 때문에 ForeignKey 를 생성할때 모델의 이름만 명시해주어도 되는 구조를 갖는다.
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    instructor_name = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.instructor_name


    class Meta:
        ordering = ('instructor_name',)


class LectureRoom(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    lecture_room_name = models.CharField(max_length=100, blank=False)
    lecture_room_address = models.CharField(max_length=100, blank=False)
    lecture_room_latitude = models.FloatField()
    lecture_room_longitude = models.FloatField()


    def __str__(self):
        return self.lecture_room_name


    class Meta:
        ordering = ('lecture_room_name', 'lecture_room_address',)


class Lecture(models.Model):
    '''
    Lecture 모델과 Instructor 모델의 관계 : Many To Many
    - 하나의 강의에 여러 강사가 참여 할 수 있고, 동시에 한명의 강사가 여러 강의에 참여 할 수 있으므로!
      Django 에서 Many To Many 관계를 갖는 경우, ManyToManyField 를 사용한다.

    Lecture 모델과 LectureRoom 모델의 관계 : One To Many
    - 강의실은 타 강의에도 사용 할 수 있어 등록해두면 이후에 진행되는 강의에도 활용 할 수 있으나,
      강의는 단 한번만 열리는 1회성이라는 특징을 가지고 있으므로 One To Many 관계를 갖는다.
      Django 에서 One To Many 관계를 갖는 경우, ForeignKey 를 사용한다.
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    lecture_title = models.CharField(max_length=100, blank=False)
    start_datetime = models.DateTimeField(blank=False)
    end_datetime = models.DateTimeField(blank=False)
    instructors = models.ManyToManyField(Instructor)
    lecture_room = models.ForeignKey(LectureRoom, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.lecture_title


    class Meta:
        ordering = ('lecture_title', 'start_datetime', 'end_datetime', )