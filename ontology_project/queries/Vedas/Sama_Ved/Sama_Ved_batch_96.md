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

### Verse 1 (Sama Ved 0.1901)
- **Original**: तृम्पा व्यश्नुही मदम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1902)
- **Original**: हे बलशाली इन्द्रदेव ! सोमयज्ञ में आपके लिए सोमरस शोधित किया है । उस आनन्ददायी रस का पानकर आप तृप्त हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1903)
- **Original**: 732.मा त्वा मूरा अविष्यवों मोपहस्वान आ दभन्‌। मा की ब्रह्मद्विषं वनः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1904)
- **Original**: हे इन्द्रदेव ! आपसे रक्षण की कामना करने वाले तथा उपहास करने वाले अज्जानियों का आप पर प्रभाव न पढ़े । ज्ञान द्रेषियों की आप मदद न करूँ
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1905)
- **Original**: 733.इह त्वा गोपरीणसं महे मन्दन्तु राधसे । सरो गौरो यथा पिब
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1906)
- **Original**: हे इद्धदेव ! गौ दुग्ध मिश्रित सोमरस की हवि देकर, होता ऐश्वर्य प्राप्त के लिए आपकी प्रार्थना करते हैं । तालाब में जल पीने वाले मृग की भाँति आप सोमरस का पान करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1907)
- **Original**: 734.इदं बसो सुतमन्धः पिबा सुपूर्णमुदरम्‌। अनाभयिद्ररिमा ते
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1908)
- **Original**: हे आश्रयदाता, निर्भव इन्द्रदेव ! जी भर कर पीने के लिए हम आपको शोधित सोमरस देते हैं, आप उसका पान करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1909)
- **Original**: 735.नृभिधौत: सुतो अश्नैरव्या बारैः परिपूत:। अश्वो न निक्‍तो नदीषु
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1910)
- **Original**: जिस प्रकार घोड़े को जलाशय में स्वच्छ किया जाता है, उसी प्रकार याजकों द्वारा सोम (सोमलता को) स्वच्छ करके, पत्थरों से कूटकर, छलनी में छान कर यह सोमरस तैयार किया गया है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1911)
- **Original**: 736.त॑ ते यव॑ यथा गोभिः स्वादुमकर्म श्रीणन्तः । इन्द्र त्वास्मिन््सधमादे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1912)
- **Original**: है इद्धदेव ! पुरोडाश की भाँति गाय के दूध में मिला कर शोधित यह मधुर सोमरस आपके लिए तैयार किया गया है । इस आनन्ददायी सोमपान के लिए हम आपका आवाहन करते हैं । ।12
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1913)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1914)
- **Original**: के के के
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1915)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1916)
- **Original**: 737, इद ह्न्वोजसा सुतं राधानां पते
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1917)
- **Original**: पिबा त्वा3स्य गिर्वण:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1918)
- **Original**: हे धनपति, स्तुत्य, बलशाली इन्द्रदेव ! आप रुचिपूर्वक इस सोमरस का पान करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1919)
- **Original**: 738.यस्ते अनु स्वधामसत्सुते नि यच्छ तन्वम्‌। स त्वा ममत्तु सोम्य
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1920)
- **Original**: हे सोमपान के योग्य इन्द्रदेव ! आपके शरीर के लिए यह सोम अनतुल्य है । यज्ञ में उपस्थित होकर आप इसके पान से आनन्दित हों
- **Translation**: 

---

