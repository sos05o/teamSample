from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Department(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='部署ID')
    name = models.CharField(max_length=24, verbose_name='部署名')

    def __str__(self):
        return self.name


class Position(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='役職ID')
    name = models.CharField(max_length=5, verbose_name='役職名')

    def __str__(self):
        return self.name


class User_info(models.Model):
    id = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],
                             primary_key=True, verbose_name='社員ID')
    firstName = models.CharField(max_length=16, verbose_name='姓')
    lastName = models.CharField(max_length=16, verbose_name='名')
    birth = models.DateField(verbose_name='生年月日')
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    pos_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    boss_id = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],
                                  verbose_name='上司ID')
    mailAddress = models.CharField(max_length=64, verbose_name='メールアドレス')
    salt = models.CharField(max_length=32, verbose_name='ソルト')
    hashed_pw = models.CharField(max_length=64, verbose_name='パスワード')

    def __str__(self):
        return self.id


class Ringisyo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='稟議書ID')
    title = models.CharField(max_length=32, verbose_name='稟議書タイトル')
    auth_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    deadline = models.DateField(verbose_name='承認期限')
    product_title = models.CharField(max_length=32, verbose_name='物品名')
    trader_name = models.CharField(max_length=32, verbose_name='業者名')
    quantity = models.IntegerField(verbose_name='数量')
    unit_price = models.IntegerField(verbose_name='単価')
    need_reason = models.CharField(max_length=512, verbose_name='必要理由')
    trader_reason = models.CharField(max_length=512, verbose_name='業者選定理由')

    def __str__(self):
        return self.title


class Purchase_Flag(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='購入フラグID')
    flag = models.CharField(max_length=5, verbose_name='購入フラグ')

    def __str__(self):
        return self.flag


class Approval_Flag(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='承認フラグID')
    flag = models.CharField(max_length=5, verbose_name='承認フラグ')

    def __str__(self):
        return self.flag


class Ringisyo_apv(models.Model):
    id = models.OneToOneField(Ringisyo, on_delete=models.CASCADE, primary_key=True)
    purchase = models.ForeignKey(Purchase_Flag, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=512, verbose_name='備考')

    chief_apv = models.ForeignKey(Approval_Flag, related_name='chief',
                                  on_delete=models.CASCADE, verbose_name='主任_承認')

    director_apv = models.ForeignKey(Approval_Flag, related_name='director',
                                     on_delete=models.CASCADE, verbose_name='部長_承認')

    mDirector_apv = models.ForeignKey(Approval_Flag, related_name='mDirector',
                                      on_delete=models.CASCADE, verbose_name='常務_承認')

    president_apv = models.ForeignKey(Approval_Flag, related_name='president',
                                      on_delete=models.CASCADE, verbose_name='社長_承認')

    def __str__(self):
        return Ringisyo.title
