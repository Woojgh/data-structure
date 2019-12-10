import pytest

from linked_list import LinkedList, Node


@pytest.fixture
def ll():
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)
  return ll


def test_LinkedList_exsists():
  assert LinkedList()


def test_node_exsists():
  assert Node(0)


def test_LinkedList_head_instantiates_as_none():
  ll = LinkedList()
  assert ll.head == None


def test_node_insert():
  ll = LinkedList()
  ll.insert(1)
  assert ll.head.value == 1
  assert ll.head.next == None


def test_node_insert_seccond_node():
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  assert ll.head.value == 2
  assert ll.head.next.value == 1
  assert ll.head.next.next == None


def test_node_insert_many_node(ll):
  assert ll.head.value == 3
  assert ll.head.next.value == 2
  assert ll.head.next.next.value == 1
  assert ll.head.next.next.next == None


def test_includes(ll):
  assert ll.includes(1) is True


def test_does_not_include(ll):
  assert ll.includes(357) is False


def test_includes_at_head(ll):
  assert ll.includes(3) is True
