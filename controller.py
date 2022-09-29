from inspect import _void
from data.parse_data import LOCAL_DATA
from model.Flight import Flight
from model.Timeline import Timeline

local = LOCAL_DATA


def question10() -> None:

    local.get_greatest_numbers_passengers()


def question_one() -> int:
    # What is the total number of passages sold among all the flights?
    total_passages_sale = local.get_number_of_passages_sale()

    return total_passages_sale


def question_two() -> float:
    # What is the total income from the sale of economic passages?
    total_income_economic_passages = sum(
        v.get_total_income_by_economic_passages() for v in local.flights)

    return total_income_economic_passages


def question_three() -> float:
    # What is the total income from the sale of premium passages?
    total_income_premium_passages = sum(
        v.get_total_income_by_premium_passages() for v in local.flights)

    return total_income_premium_passages


def question_four() -> float:
    # What is the total amount of IGV charged?
    total_IGV_Charge = sum(v.get_total_IGV_charge() for v in local.flights)

    return total_IGV_Charge


def question_five() -> float:
    # What is the average value of an economic passage?
    total_passages_sale: float = float(local.get_number_of_economic_passages())
    total_income_economic_passages: float = sum(
        v.get_total_income_by_economic_passages() for v in local.flights)
    average_economic_passage = total_income_economic_passages / total_passages_sale

    return average_economic_passage


def question_six() -> float:
    # What is the average value of a premium passage?
    total_passages_sale: float = float(local.get_number_of_premium_passages())
    total_income_economic_passages: float = sum(
        v.get_total_income_by_economic_passages() for v in local.flights)
    average_economic_passage: float = total_income_economic_passages / total_passages_sale

    return average_economic_passage
