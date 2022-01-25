from django.db import models


class Cliente(models.Model):
    SEXO_CHOICES = (("feminino", "Feminino"), ("masculino", "Masculino"), )
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=11, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome


class Locadora(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cnpj = models.CharField(max_length=20, null=False)
    cidade = models.CharField(max_length=20, null=False)
    logadouro = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome


class Acessorio(models.Model):
    ESTADO_CHOICES = (
        ("ótimo", "Ótimo"),
        ("bom", "Bom"),
        ("ruim", "Ruim"),
    )
    descricao = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, null=False)

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    CORES_CHOICES = (
        ("preto", "Preto"),
        ("azul", "Azul"),
        ("amarelo", "Amarelo"),
        ("branco", "Branco"),
        ("prata", "Prata"),
        ("vermelho", "Vermelho"),
        ("outro", "Outro"),
    )
    TIPO_CHOICES = (
        ("moto", "Moto"),
        ("carro", "Carro"),
        ("van", "Van"),
        ("ônibus", "Ônibus"),
        ("outro", "Outro"),
    )
    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    placa = models.CharField(max_length=8, null=False)
    cor = models.CharField(max_length=20, null=False, choices=CORES_CHOICES)
    ano = models.IntegerField(null=False)
    locadora = models.ForeignKey(Locadora, on_delete=models.CASCADE, null=True)
    preco = models.FloatField(null=False)
    foto_capa = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    acessorios = models.ManyToManyField(Acessorio, null=True, blank=True)

    def aluguel_diario(self):
        return self.preco * 0.001

    def __str__(self):
        return self.modelo


class Aluguel(models.Model):
    PAGAMENTO_CHOICES = (
        ("dinheiro", "Dinheiro"),
        ("cartão de credito", "Cartão de Crédito"),
        ("cartão de debito", "Cartão de Débito"),
    )
    data_aluguel = models.DateField(null=False, verbose_name="Data de aluguel")
    data_devolucao = models.DateField(null=False, verbose_name="Data de devolução")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pagamento = models.CharField(max_length=20, choices=PAGAMENTO_CHOICES, null=True)

    def preco_total(self):
        quantidade_dias = abs((self.data_devolucao - self.data_aluguel).days)
        return self.veiculo.preco_diario * quantidade_dias

    def __str__(self):
        return str(self.cliente)
