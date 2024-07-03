import string
from estnltk import Text
from estnltk.taggers import TokensTagger, SpellCheckRetagger
from google.protobuf.json_format import ParseDict
from mediapipe.framework.formats import landmark_pb2


def preprocess_phrase(phrase):

    phrase = phrase.lower()

    phrase = phrase.translate(str.maketrans('', '', string.punctuation))

    phrase = phrase.strip()

    text = Text(phrase)

    # Tokenization
    TokensTagger().tag(text)

    # Add the 'words' layer needed for spell correction
    text.tag_layer(['words'])

    # Spell correction
    spellcheck_tagger = SpellCheckRetagger()
    spellcheck_tagger.retag(text)

    # Extract original tokens
    tokens = [token.text for token in text['tokens']]

    # Extract spell-corrected tokens
    corrected_tokens = []
    for token in text['words']:
        if token.normalized_form[0] is not None:
            corrected_tokens.append(token.normalized_form[0])
        else:
            corrected_tokens.append(token.text)


    return corrected_tokens


def create_normalized_landmark_proto(landmarks_list):
    # Use ParseDict to convert dictionary to NormalizedLandmark object
    return [ParseDict(lm, landmark_pb2.NormalizedLandmark()) for lm in landmarks_list]