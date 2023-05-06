from dataclasses import dataclass

@dataclass
class configuration_parameters:
    DATALAKE: str
    CONTAINER: str
    SASKEY: str


PARAMETERS = configuration_parameters (
DATALAKE="https://itechdayadla.dfs.core.windows.net",
CONTAINER="demolearn",
SASKEY="?sv=2022-11-02&ss=bfqt&srt=sc&sp=rwdlacupyx&se=2023-05-31T09:27:54Z&st=2023-05-06T01:27:54Z&spr=https&sig=kvedG7707y8H%2FE8ZNsrEIOl7L2AhS3X0QEqtXi0GoJg%3D"
)