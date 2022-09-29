
from config.config import CURRENCY
from data.parse_data import LOCAL_DATA

local = LOCAL_DATA


def question10() -> None:

    local.get_greatest_numbers_passengers()


def question_nine() -> str:
    local.get_the_first_three_flights_with_the_highest_sales()


def question_one() -> None:
    # What is the total number of passages solds among all the flights?
    total_passages_sale = local.get_number_of_passages_sale()
    print(f"1.- Total number of passages solds: {total_passages_sale}")


def question_two() -> None:
    # What is the total income from the sale of economic passages?
    total_income_economic_passages = round(sum(
        v.get_total_income_by_economic_passages() for v in local.flights), 2)
    print(
        f"2.- Total income from economic passages: {CURRENCY} {total_income_economic_passages}")


def question_three() -> None:
    # What is the total income from the sale of premium passages?
    total_income_premium_passages = round(sum(
        v.get_total_income_by_premium_passages() for v in local.flights), 2)
    print(
        f"3.- Total income from premium passages: {CURRENCY} {total_income_premium_passages}")


def question_four() -> None:
    # What is the total amount of IGV charged?
    total_IGV_Charge: float = round(
        sum(v.get_total_IGV_charge() for v in local.flights), 2)
    print(f"4.- Total amount of IGV charged: {CURRENCY} {total_IGV_Charge}")


def question_five() -> None:
    # What is the average value of economic passages?
    total_passages_sale: float = float(local.get_number_of_economic_passages())
    total_income_economic_passages: float = sum(
        v.get_total_income_by_economic_passages() for v in local.flights)
    average_economic_passage: float = round(
        total_income_economic_passages / total_passages_sale, 2)
    print(
        f"5.- Average value of economic passages: {CURRENCY} {average_economic_passage}")


def question_six() -> None:
    # What is the average value of a premium passage?
    total_passages_sale: float = float(local.get_number_of_premium_passages())
    total_income_premium_passages: float = sum(
        v.get_total_income_by_premium_passages() for v in local.flights)
    average_premium_passage: float = round(
        total_income_premium_passages / total_passages_sale, 2)
    print(
        f"6.- Average value of premium passages: {CURRENCY} {average_premium_passage}")
