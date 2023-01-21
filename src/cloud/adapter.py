from abc import ABC, abstractmethod


class AbstractAdapter(ABC):
    @abstractmethod
    def upload(path, to):
        pass

    @abstractmethod
    def delete(path):
        pass

    @abstractmethod
    def mkdir(path):
        pass


class MailRuAdapter(AbstractAdapter):
    def upload(self, path, to):
        self.client.create()

    def delete(self, path):
        self.client.delete(path)


class YandexAdapter(AbstractAdapter):
    def upload(self, path, to):
        self.client.create_file()

    def delete(self, path):
        self.client.delete_from_cloud(path)
