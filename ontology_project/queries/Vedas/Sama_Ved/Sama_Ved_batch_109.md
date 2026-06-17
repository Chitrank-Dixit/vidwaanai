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

### Verse 1 (Sama Ved 0.2161)
- **Original**: प्रथम: खण्ड: ।
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2162)
- **Original**: . <30,एते असृम्रमिन्दवस्तिर: पवित्रमाशव: । विश्वान्यत्रि सौभगा
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2163)
- **Original**: छन्‍ने को ओर द्रुतगति से जाते हुए सोमरस को, सभी सौभाग्यों की प्राप्ति के लिए, क्र््रत्विजों द्वारा शोधित किया जाता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2164)
- **Original**: 831.विध्नन्तो दुरिता पुरु सुगा तोकाय वाजिन: । त्मना कृण्वन्तों अर्वत:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2165)
- **Original**: बलवर्धक, पापनाशक यह सोमरस हमारे व हमारी सत्तति के लिए पशुधन प्रदान करने-का मार्ग स्वयं बनाता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2166)
- **Original**: <832.कृण्वन्तो वरिवो गवे5 भ्यर्षन्ति सुष्ठतिम्‌। इडामस्मभ्यं संयतम्‌
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2167)
- **Original**: हमारे लिए एवं हमारी गौओं के लिए उत्तम धन तथा पौष्टिक अन के प्रदाता सोभदेव, हमारी सुन्दर प्रार्थनाओं को स्वीकार करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2168)
- **Original**: 833.राजा मेधाभिरीयते पवमानो मनावधि
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2169)
- **Original**: अन्तरिक्षेण यातवे
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2170)
- **Original**: मानवों द्वारा किये गये यज्ञों से शुद्ध होने बाला यह राजा (रसराज) सोम, विचारपूर्वक की गयी स्तुतियों के प्रभाव से अंतरिक्ष में संचारित होता हुआ कलश (धारण करने वाले माध्यमों) कौ ओर बढ़ता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2171)
- **Original**: <34.आ नः सोम सहो जुबो रूप॑ न वर्चसे भर
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2172)
- **Original**: सुष्वाणो देववीतये
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2173)
- **Original**: देवी शक्तियों के लिए शोधित हे सोमदेव ! आप बलवर्द्धक बनकर हमें ऐसी शक्ति प्रदान करें, जिससे हमारी तेजस्विता बढ़े
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2174)
- **Original**: 835.आ न इन्दो शातग्विन॑ गवां पोष॑ स्वश्व्यम्‌। वहा भगत्तिमूतये
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2175)
- **Original**: है सोम आप सैकड़ों गौओं एवं श्रेष्ठ घोड़ों की प्राप्ति और उनका पोषण करने में समर्थ हैं। आप हमें सौभाग्य प्रदान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2176)
- **Original**: 836.त॑ त्वा नृम्णानि बिश्रतं सधस्थेषु महो दिवः । चारुं सुकृत्ययेमहे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2177)
- **Original**: देवलोक में व्याप्त नाना प्रकार के ऐश्वर्यों से युवत्‌ सुन्दर हे सोमदेब ! उत्तम कर्मों (यज्ञों) के द्वारा आपको प्राप्त करने की हमारी कामना है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2178)
- **Original**: <37.संवृक्तथृष्णुमुक्थ्यं महामहित्रतं मदम्‌। शत पुरो रुरुक्षणिम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2179)
- **Original**: है असुरजयी सोमदेव ! आप उत्तम कर्म करने वाले आनन्ददायी तथा शत्रुओं के सैकड़ों नगरों को ध्वंस करले वाले हैं। आपसे हम ऐश्वर्य की याचना करते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2180)
- **Original**: डर सामवेद-संहिता 838.अतस्त्वा रविरभ्ययद्राजान॑ सुक्रतो दिव:। सुपर्णों अव्यथी भरत्‌
- **Translation**: 

---

