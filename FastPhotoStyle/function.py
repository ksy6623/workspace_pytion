# function.py
import torch
import numpy as np


def coral(source, target):
    """
    CORAL: Correlation Alignment for Deep Domain Adaptation
    Align the distribution of source to target.
    """
    source = source.double()
    target = target.double()

    # Flatten
    source_mean = torch.mean(source, dim=2, keepdim=True)
    source = source - source_mean
    target_mean = torch.mean(target, dim=2, keepdim=True)
    target = target - target_mean

    # Compute covariance
    source_cov = source.bmm(source.transpose(1, 2)) / (source.size(2) - 1)
    target_cov = target.bmm(target.transpose(1, 2)) / (target.size(2) - 1)

    # Whitening source
    source_eigvals, source_eigvecs = torch.linalg.eigh(source_cov)
    source_d = source_eigvals.clamp(min=1e-5).rsqrt()
    whiten = source_eigvecs.bmm(torch.diag_embed(source_d)).bmm(source_eigvecs.transpose(1, 2))

    source = whiten.bmm(source)

    # Coloring with target
    target_eigvals, target_eigvecs = torch.linalg.eigh(target_cov)
    target_d = target_eigvals.clamp(min=1e-5).sqrt()
    color = target_eigvecs.bmm(torch.diag_embed(target_d)).bmm(target_eigvecs.transpose(1, 2))

    source = color.bmm(source)
    source = source + target_mean

    return source.float()


def preserve_color(style, content):
    """
    Adjust style image's color distribution to match content image using histogram matching.
    Only supports tensors in shape (1, 3, H, W).
    """
    s = style.clone().squeeze(0).cpu().numpy()
    c = content.clone().squeeze(0).cpu().numpy()

    for i in range(3):
        s_mean = s[i].mean()
        s_std = s[i].std()
        c_mean = c[i].mean()
        c_std = c[i].std()
        s[i] = ((s[i] - s_mean) * (c_std / (s_std + 1e-5))) + c_mean

    style = torch.from_numpy(s).unsqueeze(0)
    return style.to(content.device)
