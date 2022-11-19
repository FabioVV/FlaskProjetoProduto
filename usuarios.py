from dataclasses import dataclass


@dataclass(frozen=True)
class InformacoesUsuarioSemSenha:
    login: str
    nome: str


@dataclass(frozen=True)
class userdata:
    login: str
    nome: str
    senha: str

    @property
    def sem_senha(self) -> InformacoesUsuarioSemSenha:
        return InformacoesUsuarioSemSenha(self.login, self.nome)


class UsuarioJaExiste(Exception):
    pass


class SenhaIncorreta(Exception):
    pass


class user:
    def __init__(self):
        self.__users = {}

    def novo_user(self, login: str, nome: str, senha: str):
        if login in self.__users:
            raise UsuarioJaExiste
        us = userdata(login, nome, senha)
        self.__users[login] = us

    def validar_login(self, login: str, senha: str):
        if login not in self.__users:
            raise SenhaIncorreta
        u = self.__users[login]
        if u.senha != senha:
            raise SenhaIncorreta
        return u.sem_senha

    def revalidar(self, login: str):
        if login not in self.__users:
            return None
        return self.__users[login].sem_senha

    def name(self):
        return userdata.nome
