import timm
from timm.data import resolve_data_config

from torch import nn

class TimmModel(nn.Module):
    def __init__(
        self,
        model_name
    ):
        super().__init__()

        self.model_name = model_name
        print(f'creating {model_name} from timm...')
        self.model = timm.create_model(self.model_name, pretrained=True)

    def get_data_config(self):
        config = resolve_data_config({}, model=self.model)
        return config

    def forward(self, x):
        return self.model(x)


if __name__ == "__main__":
    import hydra
    import omegaconf
    import pyrootutils

    root = pyrootutils.setup_root(__file__, pythonpath=True)
    cfg = omegaconf.OmegaConf.load(root / "configs" / "model" / "timm.yaml")
    test_model = hydra.utils.instantiate(cfg.net)
    print(test_model.model_name.upper())
