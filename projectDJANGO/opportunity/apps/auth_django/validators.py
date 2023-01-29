from rest_framework.exceptions import AuthenticationFailed


class validateUser:
    @staticmethod
    def verify_user(user):
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

    @staticmethod
    def authorized_user(user):
        if not user.verify_staff_user:
            raise AuthenticationFailed(
                'You have not been verified by the system as a valid user for authentication')

    @staticmethod
    def user_not_active(user):
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

    @staticmethod
    def user_not_verified(user):
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

    validadores_usuarios = {
        'usuario_falso': lambda user: validateUser.verify_user(user),
        'usuario_nao_autorizado': lambda user:  validateUser.authorized_user(user),
        'usuario_nao_ativo': lambda user: validateUser.user_not_active(user),
        'usuario_nao_verificado': lambda user: validateUser.user_not_verified(user)

    }
