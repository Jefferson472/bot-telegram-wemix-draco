import requests


class Crypto_Price:
    def get_price(self, url, crypto):
        request = requests.post(url, verify=False)
        response_json = request.json()
        crypto_price = response_json['Data'][crypto]
        request.close()
        return crypto_price[0:4]

    def get_draco_wemix_price(self):
        draco_wemix_price = self.get_price(
            'https://api.mir4global.com/wallet/prices/draco/lastest',
            'USDDracoRate',
            )
        return "${0:3} USD".format(draco_wemix_price)

    def get_hidra_wemix_price(self):
        hidra_wemix_price = self.get_price(
            'https://api.mir4global.com/wallet/prices/hydra/lastest',
            'USDHydraRate',
            )
        return "${0:3} USD".format(hidra_wemix_price)


if __name__ == '__main__':
    crypto_price = Crypto_Price()
    print(crypto_price.get_draco_wemix_price())
    print(crypto_price.get_hidra_wemix_price())
