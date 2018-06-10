from django.db import models


class Jogadores(models.Model):

    POSICAO_CHOICES = (
        ('GL', 'Goleiro'),
        ('ZA','Zagueiro'),
        ('LT','Lateral'),
        ('MC','Meio Campo'),
        ('AT','Atacante')
    )
    nome = models.CharField(max_length=70)
    posicao = models.CharField(choices=POSICAO_CHOICES, max_length=15)
    cartoes_amarelos = models.IntegerField(null=True)
    cartao_vermelho = models.IntegerField(null=True)
    gols = models.IntegerField(null=True)
    nacionalidade = models.CharField(max_length=70)

    def __str__(self):
        return self.nome
    

class Time(models.Model):

    STATUS_CHOICES = (
        ('ELIMINADO','Eliminado'),
        ('COMPETINDO','Competindo'),
        ('CAMPEAO','Campeão')
    )
    nome = models.CharField(max_length=70)
    gols_marcados = models.IntegerField(null=True)
    gols_sofridos = models.IntegerField(null=True)
    vitorias = models.IntegerField(null=True)
    derrotas = models.IntegerField(null=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=15)
    competicao = models.CharField(max_length=70)
    jogador = models.ForeignKey(Jogadores,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Grupos(models.Model):
    nome = models.CharField(max_length=70)
    time = models.ManyToManyField(Time)

    def __str__(self):
        return self.nome


class Partidas(models.Model):
    data = models.DateField()
    adversarioA = models.ForeignKey(Time,on_delete=models.CASCADE)
    # adversarioB = models.OneToOneField(Time,on_delete=models.CASCADE)
    # adversarioB = models.ForeignKey(Time,related_name='%(class)add_adversarios',on_delete=models.CASCADE)
    # resultado 
    local = models.CharField(max_length=70)

