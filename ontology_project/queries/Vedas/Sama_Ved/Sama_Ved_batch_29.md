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

### Verse 1 (Sama Ved 0.561)
- **Original**: 202. इन्द्रा नु पृषणा वयं सख्याय स्वस्तये । हुवेम वाजसातये
- **Translation**: 

---

### Verse 2 (Sama Ved 0.562)
- **Original**: अन प्राप्ति की कामना से, अपने कल्याण के लिए मित्रवत्‌ इन्द्र और पूषा देवताओं को स्तुतियों के द्वारा हम उलाते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.563)
- **Original**: 203. न कि इन्द्र त्वदुत्तरं न ज्यायो अस्ति वृत्रहन्‌ । न क्‍्येव॑ यथा त्वम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.564)
- **Original**: हे शत्रु संहारक इन्द्रदेव ! आपसे अधिक श्रेष्ठ और महान्‌ दूसरा कोई नहीं हैं । आपके समान अन्य और कोई नहीं है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.565)
- **Original**: इति नवम: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.566)
- **Original**: के ओऔ के
- **Translation**: 

---

### Verse 7 (Sama Ved 0.567)
- **Original**: दशम: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.568)
- **Original**: 204, तरणिं वो जनानां त्रदं वाजस्य गोमत: । समानमु प्र शंसिषम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.569)
- **Original**: ( हे स्तोताओ) लोगों को बाधाओं से पार कराने वाले, शत्रु को भयभीत करने वाले, पशुधन से सम्पन्न अन का दान करने वाले, उन्‍नतिशील इन्द्रदेव की हम स्तुति करते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.570)
- **Original**: 205. असुग्रमिन्द्र ते गिर: प्रति त्वामुदहासत
- **Translation**: 

---

### Verse 11 (Sama Ved 0.571)
- **Original**: सजोषा वृषभं पतिम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.572)
- **Original**: । हे इन्द्रदेव ! आपकी स्तुति के लिए हमने स्तोत्रों की रचना की है । बलशाली और पालनकर्ता इन्द्रदेव, इन स्तुतियों से हमने आपकी प्रार्थना की है, जिसे आपने स्वीकार किया है.
- **Translation**: 

---

### Verse 13 (Sama Ved 0.573)
- **Original**: 206. सुनीथो घा स मर्त्यों यं मरुतो यमर्यमा । मित्रास्पान्त्यद्रुह:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.574)
- **Original**: द्रोह रहित मरुतू, मित्र और अर्यमा, जिस साधक के रक्षक हैं, बह साधक निश्चित रूप से श्रेष्ठ पथगामी होता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.575)
- **Original**: 207. यद्वीडाविन्द्र यत्स्थिरे यत्प्शाने पराभृतम्‌। वसु स्पा तदा भर
- **Translation**: 

---

### Verse 16 (Sama Ved 0.576)
- **Original**: हे इन्द्रदेव ! पुरुषार्थ से उपार्जित, स्थिर एवं मजबूत आधार प्रदान कराने वाला उत्तम धन, जो आपके पास है, वह हमें प्राप्त करायें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.577)
- **Original**: 208, श्रुतं वो बृत्रहन्तमं प्र शर्थ चर्षणीनाम्‌। आशिषे राधसे महे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.578)
- **Original**: तुमने वृत्र संहारक-बलकी महिमा सुनी ही है । मनृष्य मात्र को श्रेष्ठ धन उपलब्ध कराने की कामना से वह महान्‌ बल तुम्हें उपयोग के लिए देता हूँ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.579)
- **Original**: पूर्वार्चिके ऐज्रपर्वीण द्वितीयो5ध्याय: 2.11 209, अर त इन्द्र श्रवसे गमेम शूर त्वावतः । अरं श॒क्र परेमणि
- **Translation**: 

---

### Verse 20 (Sama Ved 0.580)
- **Original**: हे वीर इन्ददेव ! आपका यश हमने अनेकों बार सुना है । हे सामर्थ्यवान्‌ इद्धदेव ! आप जैसे महान्‌ देवगणों के सान्ज्थ्य में रहकर हम आनन्दित हों
- **Translation**: 

---

