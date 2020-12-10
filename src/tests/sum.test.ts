class BooleanReturnTrue {
    isTrue (){
      return true
    }
  }
describe("should be equal", () => {
    const booleanReturnTrue = new BooleanReturnTrue()
    jest.spyOn(booleanReturnTrue, 'isTrue').mockReturnValueOnce(false)
    test("one function that should fail", () => {
        expect(booleanReturnTrue.isTrue()).toBe(false)
    })
        test("one function that should not fail", () => {
        expect(booleanReturnTrue.isTrue()).toBe(true)
    })
})