from app import create_app
import unittest


class TestTimeline(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()

    def test_empty_get(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline")
            self.assertEqual(resp.status_code, 200)

    def test_get_with_date_filter(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline?startDate=2018-01-01&endDate=2019-01-01")
            self.assertEqual(resp.status_code, 200)

    def test_get_with_date_type_grouping_filter1(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline?startDate=2018-01-01&endDate=2019-01-01&Type=usual&Grouping=weekly")
            self.assertEqual(resp.status_code, 200)

    def test_get_with_date_type_grouping_filter2(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline?startDate=2018-01-01&endDate=2019-01-01&Type=cumulative&Grouping=monthly")
            self.assertEqual(resp.status_code, 200)

    def test_get_with_wrong_date(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline?startDate=2020-01-01&endDate=2019-01-01&Type=cumulative&Grouping=monthly")
            self.assertEqual(resp.status_code, 400)

    def test_get_with_brand_attr_filter1(self) -> None:
        with self.app.test_client() as c:
            resp = c.get("/api/timeline?startDate=2018-01-01&endDate=2019-01-01&Type=usual&Grouping=weekly&brand=Downy")
            self.assertEqual(resp.status_code, 200)

    def test_get_with_brand_attr_filter2(self) -> None:
        with self.app.test_client() as c:
            resp = c.get(
                "/api/timeline?startDate=2018-01-01&endDate=2019-01-01&Type=usual&Grouping=weekly&brand=Whitmor"
            )
            self.assertEqual(resp.status_code, 200)

    def test_get_with_stars_attr_filter(self) -> None:
        with self.app.test_client() as c:
            resp = c.get(
                "/api/timeline?startDate=2018-01-01&endDate=2019-01-01&Type=usual&Grouping=weekly&stars=5"
            )
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
