from django.db import models


class ObjectManager(models.Manager):        # Фильтрует все объекты с пометкой удалено
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(models.Model):       # Описываем модель хранения в БД новостей\
    objects = ObjectManager()
    title = models.CharField(max_length=256, verbose_name="Title")  # Заголовок новости
    preambule = models.CharField(max_length=1024, verbose_name="Preambule")  # Краткое описание новости
    body = models.TextField(blank=True, null=True, verbose_name="Body")  # Тело новости
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)        # Отметка об удалении

    def __str__(self) -> str:   # Описываем форму при вызове print
        return f"{self.pk} {self.title}"        # ИД и заголовок

    def delete(self, *args):        # При вызове передает значение True
        self.deleted = True
        self.save()


class Courses(models.Model):       # Описываем модель хранения в БД курсов
    objects = ObjectManager()
    name = models.CharField(max_length=256, verbose_name="Name")        # Название курса
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cost", default=0)      # Цена курса
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Lesson(models.Model):       # Описываем модель хранения в БД уроков
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)       # Привязка к курсу
    num = models.PositiveIntegerField(verbose_name="Lesson number")     # Номер урока
    title = models.CharField(max_length=256, verbose_name="Name")       # Название урока
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Meta:
    ordering = ("course", "num")


class CourseTeachers(models.Model):     # Описываем модель хранения в БД преподавателей
    course = models.ManyToManyField(Courses)
    first_name = models.CharField(max_length=128, verbose_name="Name")
    second_name = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.second_name, self.first_name)

    def delete(self, *args):
        self.deleted = True
        self.save()
