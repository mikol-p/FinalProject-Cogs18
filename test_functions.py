import classes as cls
import functions as fns

def test_displayer_function(): 
    
    pass_list = {'Insta': {'Michael1': 'v%4D$*KP'}, 
                 'Facebook': {'Michaellll': 'H6!w9QU*?'}, 
                 'deletethis': {'fsojs': 'R?a6ut7w'}}

    # Should return nothing as this functions only prints the passwords neatly
    assert fns.display_passwords(pass_list) == None 
    

def test_encoder_function():

    pass_list = {'Insta': {'Michael1': 'v%4D$*KP'}, 
                 'Facebook': {'Michaellll': 'H6!w9QU*?'}, 
                 'deletethis': {'fsojs': 'R?a6ut7w'}}

    assert fns.encoder(pass_list) == 'đĶĻļĩèĕıīİĩĭĴùèľíüČìòēĘèĎĩīĭĪķķĳèĕıīİĩĭĴĴĴĴèĐþéĿāęĝòćèĬĭĴĭļĭļİıĻèĮĻķĲĻèĚćĩþĽļÿĿè'


def test_decoder_function():

    encoded = 'đĶĻļĩèĕıīİĩĭĴùèľíüČìòēĘèĎĩīĭĪķķĳèĕıīİĩĭĴĴĴĴèĐþéĿāęĝòćèĬĭĴĭļĭļİıĻèĮĻķĲĻèĚćĩþĽļÿĿè'

    # Should return nothing but print the decoded password list neatly
    assert fns.decoder(encoded) == None