import pytest
from src.util.detector import detect_duplicates
from src.util.parser import Article
from src.main import load_data

# develop your test cases here



data_duplicates = """
@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
}

@article{fernandez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{mendez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{wagner2019status,
  title={Status quo in requirements engineering: A theory and a global family of surveys},
  author={Wagner, Stefan and M{\'e}ndez Fern{\'a}ndez, Daniel and Felderer, Michael and Vetr{\`o}, Antonio and Kalinowski, Marcos and Wieringa, Roel and Pfahl, Dietmar and Conte, Tayana and Christiansson, Marie-Therese and Greer, Desmond and others},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={28},
  number={2},
  pages={1--48},
  year={2019},
  publisher={ACM New York, NY, USA}
}

@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer}
}
"""

data_no_duplicates = """
@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
}

@article{fernandez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{mendez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{wagner2019status,
  title={Status quo in requirements engineering: A theory and a global family of surveys},
  author={Wagner, Stefan and M{\'e}ndez Fern{\'a}ndez, Daniel and Felderer, Michael and Vetr{\`o}, Antonio and Kalinowski, Marcos and Wieringa, Roel and Pfahl, Dietmar and Conte, Tayana and Christiansson, Marie-Therese and Greer, Desmond and others},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={28},
  number={2},
  pages={1--48},
  year={2019},
  publisher={ACM New York, NY, USA}
}
"""

data_few = """
@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
}
"""

txt = 'data/references.txt'

@pytest.mark.unit
def test_detect_duplicates_has_duplicates():
    result = detect_duplicates(data_duplicates)
    duplicate = [Article("frattini2023requirements")]
    assert result == duplicate

@pytest.mark.unit
def test_detect_duplicates_no_duplicates():
    result = detect_duplicates(data_no_duplicates)
    assert result == None


@pytest.mark.unit
def test_detect_duplicates_few_articles():
    with pytest.raises(ValueError):
        detect_duplicates(data_few)

@pytest.mark.unit
def test_detect_duplicates_wrong_format():
    data = load_data(txt)
    with pytest.raises(TypeError):
        detect_duplicates(data)

# I structured the test cases by deriving them from the table of test cases that I created, by consulting both the docstring of the unit and the specification.
# I ensured test independence by not making them relying on each other (if one test fails it should not cause the following tests to fail), and with the exception
# of the test that tests if the file is in wrong format, the data is hard-coded into the test file
# Ie experienced some challenges when implementing the test that finds a duplicate; it took a while to understand that I needed to use the Article class when asserting,
# since using a normal list with strings did not work