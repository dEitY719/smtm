import unittest
from smtm import TddExercise
from unittest.mock import *
# import requests


class TddExerciseTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_period_update_period_correctly(self):
        ex = TddExercise()
        # check default value
        self.assertEqual(ex.to, None)
        self.assertEqual(ex.count, 50)

        ex.set_period("2024-02-25T06:41:00Z", 10)

        self.assertEqual(ex.to, "2024-02-25T06:41:00Z")
        self.assertEqual(ex.count, 10)

    def test_initialize_from_server_update_data_correctly_example(self):
        ex = TddExercise()
        self.assertEqual(len(ex.data), 0)

        ex.initialize_from_server()
        self.assertEqual(len(ex.data), 50)

    @patch("requests.get")
    def test_initialize_from_server_update_data_correctly_with_empty_data(self, mock_get):
        ex = TddExercise()
        dummy_response = MagicMock()
        mock_get.return_value = dummy_response

        ex.initialize_from_server()
        self.assertEqual(len(ex.data), 0)

    @patch("requests.get")
    def test_initialize_from_server_update_data_correctly(self, mock_get):
        ex = TddExercise()
        dummy_response = MagicMock()
        dummy_response.json.return_value = [{"market": "apple"}, {"market": "banana"}]
        mock_get.return_value = dummy_response

        ex.initialize_from_server()
        self.assertEqual(len(ex.data), 2)
        self.assertEqual(ex.data[0], {"market": "apple"})
        self.assertEqual(ex.data[1], {"market": "banana"})

        mock_get.assert_called_once_with(ex.URL, params=ANY)
        self.assertEqual(mock_get.call_args[1]["params"]["count"], 50)

    def test_set_period_how_many_keys(self):
        ex = TddExercise()
        
        # 2024-09-16 기준 총 몇개인지 확인
        ex.set_period("2024-09-16T21:00:00Z", 200)

        self.assertEqual(ex.to, "2024-09-16T21:00:00Z")
        self.assertEqual(ex.count, 200)
        ex.initialize_from_server()
        self.assertEqual(len(ex.data), 200)

        # how many keys
        keys_list=ex.data[0].keys()
        
        # 키 목록 확인
        expected_keys = [
            'market', 'candle_date_time_utc', 'candle_date_time_kst', 
            'opening_price', 'high_price', 'low_price', 'trade_price', 
            'timestamp', 'candle_acc_trade_price', 'candle_acc_trade_volume', 
            'unit'
        ]

        try:
            # 키의 개수 확인
            self.assertEqual(len(keys_list), 11, f"Expected 11 keys, but got {len(keys_list)}")
            
            # 키 목록 확인
            self.assertEqual(list(keys_list), expected_keys)
            
            # 각 키가 존재하는지 개별적으로 확인
            for key in expected_keys:
                self.assertIn(key, keys_list, f"Key '{key}' is missing")

        except AssertionError as e:
            # 차이나는 키 값들 출력
            missing_keys = set(expected_keys) - set(keys_list)
            extra_keys = set(keys_list) - set(expected_keys)
            
            error_message = str(e) + "\n"
            if missing_keys:
                error_message += f"Missing keys: {', '.join(missing_keys)}\n"
            if extra_keys:
                error_message += f"Extra keys: {', '.join(extra_keys)}\n"
            
            raise AssertionError(error_message)
        
    def test_set_period_when_missing_keys(self):
        ex = TddExercise()
        
        ex.set_period("2024-09-16T21:00:00Z", 5)
        ex.initialize_from_server()
                
        # how many keys
        keys_list=ex.data[0].keys()
        
        # 키 목록 확인
        expected_keys = [
            'market', 'candle_date_time_utc', 'candle_date_time_kst', 
            'opening_price', 'high_price', 'low_price', 'trade_price', 
            'timestamp', 'candle_acc_trade_price', 'candle_acc_trade_volume', 
            'unit', 
            # 'test_missing_key',
        ]

        try:
            # 키의 개수 확인
            self.assertEqual(len(keys_list), 11, f"Expected 11 keys, but got {len(keys_list)}")
            
            # 키 목록 확인
            self.assertEqual(list(keys_list), expected_keys)
            
            # 각 키가 존재하는지 개별적으로 확인
            for key in expected_keys:
                self.assertIn(key, keys_list, f"Key '{key}' is missing")

        except AssertionError as e:
            # 차이나는 키 값들 출력
            missing_keys = set(expected_keys) - set(keys_list)
            extra_keys = set(keys_list) - set(expected_keys)
            
            error_message = str(e) + "\n"
            if missing_keys:
                error_message += f"Missing keys: {', '.join(missing_keys)}\n"
            if extra_keys:
                error_message += f"Extra keys: {', '.join(extra_keys)}\n"
            raise AssertionError(error_message)
            
        
        
    def test_set_period_when_extra_keys(self):
        ex = TddExercise()
        
        ex.set_period("2024-09-16T21:00:00Z", 5)
        ex.initialize_from_server()
                
        # how many keys
        keys_list=ex.data[0].keys()
        
        # 키 목록 확인
        expected_keys = [
            'market', 'candle_date_time_utc', 'candle_date_time_kst', 
            'opening_price', 'high_price', 'low_price', 'trade_price', 
            'timestamp', 'candle_acc_trade_price', 'candle_acc_trade_volume', 
            # 'unit', 
        ]

        try:
            # 키의 개수 확인
            self.assertEqual(len(keys_list), 11, f"Expected 11 keys, but got {len(keys_list)}")
            
            # 키 목록 확인
            self.assertEqual(list(keys_list), expected_keys)
            
            # 각 키가 존재하는지 개별적으로 확인
            for key in expected_keys:
                self.assertIn(key, keys_list, f"Key '{key}' is missing")

        except AssertionError as e:
            # 차이나는 키 값들 출력
            missing_keys = set(expected_keys) - set(keys_list)
            extra_keys = set(keys_list) - set(expected_keys)
            
            error_message = str(e) + "\n"
            if missing_keys:
                error_message += f"Missing keys: {', '.join(missing_keys)}\n"
            if extra_keys:
                error_message += f"Extra keys: {', '.join(extra_keys)}\n"
            
            print(f"{error_message=}")
            # self.assertEqual(error_message, "Extra keys: unit")
            # 예상된 차이 확인
            self.assertEqual(len(extra_keys), 1, "Expected exactly one extra key")
            self.assertIn('unit', extra_keys, "The extra key should be 'unit'")
            # raise AssertionError(error_message)