export interface Count {
  pages: number;
}

export async function getCount() {
  const url = "http://localhost:8000/count/";
  try {
    const response = await fetch(url, {
      method: "GET",
    });
    if (!response.ok) {
      throw new Error(`Response status ${response.status}`);
    }
    {
      const json = await response.json();
      console.log(`El numero total de paginas es ${json.pages}`);
      return json;
    }
  } catch (error) {
    console.log(error);
    return 0;
  }
}
