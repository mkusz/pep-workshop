import pydantic_settings

# from pydantic import SecretStr
# from pydantic import field_serializer


class UserConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(env_prefix="QA_", env_file=".env", frozen=True, extra="ignore")

    username: str = ""
    password: str = ""

    # @field_serializer("password", when_used="json")
    # def dump_secret(self, v):
    #     return v.get_secret_value()


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", env_file=".env", frozen=True, extra="ignore"
    )

    url: str = ""
