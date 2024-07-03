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

    # Extract spell-corrected tokens
    corrected_tokens = []
    for token in text['words']:
        if token.normalized_form[0] is not None:
            corrected_tokens.append(token.normalized_form[0])
        else:
            corrected_tokens.append(token.text)

    # Lemmatization
    text = ' '.join(corrected_tokens)
    text = Text(text)
    text.tag_layer()
    root_corrected_words = [tokens[0] for tokens in text.lemma]
    
    return root_corrected_words




def create_normalized_landmark_proto(landmarks_list):
    # Use ParseDict to convert dictionary to NormalizedLandmark object
    return [ParseDict(lm, landmark_pb2.NormalizedLandmark()) for lm in landmarks_list]