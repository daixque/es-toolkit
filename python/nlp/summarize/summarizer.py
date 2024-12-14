from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize(text, sentences_count=3, language="english"):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return summary

def test_english():
    text = """
    This is a sample text. This text is used to demonstrate the text summarization.
    Text summarization is the process of shortening a text document. The summary is usually shorter than the original text.
    """
    summary = summarize(text, 2)
    for sentence in summary:
        print(sentence)

def test_japanese():
    text = """
    これはサンプルテキストです。このテキストはテキスト要約をデモンストレーションするために使用されます。
    テキスト要約はテキスト文書を短縮するプロセスです。要約は通常、元のテキストよりも短くなります。
    """
    summary = summarize(text, 2, "japanese")
    for sentence in summary:
        print(sentence)

if __name__ == "__main__":
    test_english()
    # test_japanese()