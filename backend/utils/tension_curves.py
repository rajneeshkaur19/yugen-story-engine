from backend.models.tension_model import TensionCurve, Beat


def default_curve() -> TensionCurve:
    return TensionCurve(
        beats=[
            Beat(title="Whispered Beginning", description="A quiet start sets the mood.", tension=0.2),
            Beat(title="Growing Unease", description="The plot thickens with subtle tension.", tension=0.4),
            Beat(title="Rising Stakes", description="The conflict escalates.", tension=0.7),
            Beat(title="Climax", description="The emotional peak arrives.", tension=0.9),
            Beat(title="Aftermath", description="A gentle resolution unfolds.", tension=0.5),
        ]
    )
