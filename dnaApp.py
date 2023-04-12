import pandas as pd  # As usual
import streamlit
import altair as alt  # graph library
from PIL import Image  # for image

# Page Title

image = Image.open("dnalogo.jpg")

streamlit.image(
    image, use_column_width=True
)  # image should expand to column at least :)

streamlit.write(
    """
# DNA Nucleotide-Count Web App

This streamlit-powered App counts the nucleotide composition of DNA sequences.
***
"""
)

# Input DNA Sequence

streamlit.sidebar.header("DNA Neucleotide Counter - By Eric!")
streamlit.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequencesidebar = streamlit.sidebar.write("Sequence input", sequence_input, height=260)
sequence = streamlit.text_area("Sequence input", sequence_input, height=260)
sequence = sequence.splitlines()
sequence = sequence[1:]  # To skip the sequence title.
sequence = "".join(
    sequence
)  # Concatenates the seqence lines into one string to form a long stretch of Dna sequence

streamlit.write(  # *** is for the dividing line
    """
    *** 
"""
)

streamlit.header("YOUR Input (DNA Query)")
sequence

## DNA nucleotide count
streamlit.header("OUTPUT (DNA Nucleotide Count)")

### 1. Print dictionary
streamlit.subheader("1. Print dictionary")


def DNA_nucleotide_count(seq):
    info = dict(
        [
            ("A", seq.count("A")),
            ("T", seq.count("T")),
            ("G", seq.count("G")),
            ("C", seq.count("C")),
        ]
    )
    return info


result = DNA_nucleotide_count(sequence)

result

streamlit.subheader("2. Print text")
streamlit.write("There are  " + str(result["A"]) + " adenine (A)")
streamlit.write("There are  " + str(result["T"]) + " thymine (T)")
streamlit.write("There are  " + str(result["G"]) + " guanine (G)")
streamlit.write("There are  " + str(result["C"]) + " cytosine (C)")

# Display DataFrame
streamlit.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(result, orient="index")
df = df.rename({0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "nucleotide"})
streamlit.write(df)

# Display Bar Chart using Altair
streamlit.subheader("4. Display Bar chart")
p = alt.Chart(df).mark_bar().encode(x="nucleotide", y="count")
p = p.properties(width=alt.Step(100))
streamlit.write(p)
