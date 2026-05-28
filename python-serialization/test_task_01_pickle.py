#!/usr/bin/env python3
from task_01_pickle import CustomObject


def main() -> None:
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    obj.serialize("object_test.pkl")

    new_obj = CustomObject.deserialize("object_test.pkl")
    print("\nDeserialized Object:")
    if new_obj is None:
        print("Deserialization returned None")
    else:
        new_obj.display()


if __name__ == "__main__":
    main()
