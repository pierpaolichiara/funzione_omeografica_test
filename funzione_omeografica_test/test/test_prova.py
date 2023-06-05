import pytest
import funzione_omeografica_test.generate_tests as mod

@pytest.mark.parametrize("student_list, class_id, extremes", [
    (["student1", "student2"], "class1", (-10, 10)),
    (["student3", "student4"], "class2", (11, 20))
])
def test_name_generate_tests(student_list, class_id, extremes, tmp_path):
    cartella_output = tmp_path / "test_output"
    cartella_output.mkdir()

    text = '0+. -abc{}'
    mod.generate_tests(template_content_str=text, output_dir=cartella_output, student_lists=student_list,
                       function_domain=extremes, class_id=class_id)


    for student_name in student_list:
        path = cartella_output / f'test_{class_id}_{student_name}.html'
        assert path.exists()
