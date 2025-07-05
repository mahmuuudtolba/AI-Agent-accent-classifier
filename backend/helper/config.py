from pydantic_settings import BaseSettings , SettingsConfigDict 

class Settings(BaseSettings):

    APP_NAME:str
    APP_VERSION:str
    HUGGING_FACE_TOKEN:str

    model_config = SettingsConfigDict(env_file=".env")





def get_settings():
    return Settings()