# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Sama Ved 0.1861)
- **Original**: 715.इन्द्र इननो महोनां दाता वाजानां नृतु: । महाँ आभिज्ा यमत्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1862)
- **Original**: सभी को गति प्रदान करने वाले, महान्‌ इन्द्रदेव हमारे सामने प्रकट हों और हमें ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1863)
- **Original**: 716.प्र व इन्द्राय मादनं हर्यश्वाय गायत । सखायः सोमपाव्मे
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1864)
- **Original**: है स्तोताओ ! सोमरस का पान करने वाले श्रेष्ठ घोड़ों से युक्त, इन्धदेव को आनन्दित करने वाले स्तो+ सुनाओं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1865)
- **Original**: 717,शंसे दुबः्थ॑ सुदानव उत झुक्षं यथा नरः । चकृमा सत्यराधसे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1866)
- **Original**: हे त्रग्रत्विजो ! उत्तम दानदाता, न्यायोपार्जित सम्पत्ति वाले इन्द्रदेव की प्रार्थना करो । हम भी उत्तम विधि से उनकी अभ्यर्थना करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1867)
- **Original**: 718.त्वं न इन्द्र वाजयुस्त्व॑ गव्यु: शतक्रतों । त्व॑ हिरण्ययुर्वसो
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1868)
- **Original**: है पराक्रमी इद्धदेव ! आप हमें अन्न, गौ तथा स्वर्ण प्रदान करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1869)
- **Original**: 719,वयमु त्वा तदिदर्था इन्द्र त्वायन्तः सखाय:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1870)
- **Original**: कण्वा उक्थेभिर्जरन्ते
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1871)
- **Original**: हे इद्धदेव ! हम (साधक) आपको प्राप्त करने की इच्छा से सन्ततिसहित दिव्य स्तोत्रों से आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1872)
- **Original**: 720.न घेमन्यदा पपन वच्रिन्नपसो नविष्टौ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1873)
- **Original**: तवेदु स्तोमैश्चिकेत
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1874)
- **Original**: हे व्रधारी इन्द्रदेव ! यज्ञ कर्म में आपके आवाहन के सिवाय हम अन्य दूसरे की प्रार्थना नहीं करेंगे । हम स्तोत्रों द्वारा आपकी ही स्तुति करना जानते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1875)
- **Original**: 721. इच्छन्ति देवा: सुन्वन्तं न स्वप्नाय स्पृहयन्ति । यन्ति प्रमादमतन्द्रा:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1876)
- **Original**: सोमयज्ञ करने वालों से देवगण प्रसन्न रहते हैं, आलसियों से नहीं । परिश्रमी साधक ही परम आनन्दायी सोम प्राप्त करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1877)
- **Original**: 2.2 सामवेट-संहिता 722.इन्द्राय मद्ने सुतं परि ष्टोभन्तु नो गिर: । अर्कमर्चन्तु कारव:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1878)
- **Original**: आनन्ददायी सोमरस के इच्छुक इन्द्रदेव के लिए सोमरस को शोधित करने वाले हे साधको ! हमारी वाणी इन्द्रदेव की स्तुति कर रही है, स्तोतागण प्रशंसनीय सोमरस कौ स्तुति करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1879)
- **Original**: 723.यस्मिन्विश्वा अधि श्रियो रणन्ति सप्त संसद: । इन्द्र सुते हवामहे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1880)
- **Original**: उन कान्तिवान्‌ इद्धदेव का हम सोमयज्ञ में आवाहन करते हैं, जिनकी स्तुति यज्ञ के सातों 'ग्रत्विज' करते हैं
- **Translation**: 

---

