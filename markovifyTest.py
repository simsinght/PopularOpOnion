import markovify
import testString


text_model = markovify.Text(testString.string)

print(text_model.make_short_sentence(140))
