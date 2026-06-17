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

### Verse 1 (Sama Ved 0.1781)
- **Original**: 688.न य॑ दुश्वा बरन्ते न स्थिरा मुरो मदेषु शिप्रमन्धस:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1782)
- **Original**: य आदृत्या शशमानाय सुन्वते दाता जरित्र उक्थ्यम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1783)
- **Original**: 9। सुन्दर आकृति वाले इन्धरदेव को, प्राणों को बाजी लगाने वाले असुर भी नहीं हरा सकत । एसे एश्ववटाता ह इन्द्रदेव की हम स्तुति करते हैं, जो सोमरस के आनन्द में सोमयज्ञ करने वाले, भावपूर्ण स्तुतियाँ करने वाल याजकों को श्रेयस्कर अनुदान देते है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1784)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1785)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1786)
- **Original**: 689.स्वादिष्ठया मदिष्ठया पवस्व सोम धारया। इन्द्राय पातवे सुतः
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1787)
- **Original**: हे स्वादिष्ट एवं आनन्दवर्द्धक सोमदेव ! आप इद्धदेव के पोन के लिए स्नवित और परिष्कृत हों
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1788)
- **Original**: 690. रक्षेहा विश्वचर्षणिरभि योनिमयोहते । द्रोणे सधस्थमासदत्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1789)
- **Original**: दुष्ट-नाशक, मानव-हितकारी सोम शुद्ध होकर सुवर्ण पाज में रखा हुआ वज़ स्थल में प्रतिष्ठित हो गया
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1790)
- **Original**: 691.वरिवोधातमो भुवो मंहिष्ठो वृत्रहन्तम:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1791)
- **Original**: पर्षि राधो मघोनाम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1792)
- **Original**: हे सोमदेव ! आप महान्‌ ऐश्यर्य दाता हैं तथा शत्रुओं का पूर्णतय! नाश करते वाले #. इसलिये दुए प्रयोजनों में धन न लगने टेकर, उसे सत्पयोजनों में नियोजित करने के लिए प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1793)
- **Original**: 692.पवस्व मधुपत्तम इन्द्राय सोम क्रतुवित्तमो मद: । महि द्युक्षतमो मदः
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1794)
- **Original**: है सोमदेव ! आप कर्मयोगी, सुखकारी, महान्‌ तेजस्वी, आनन्ददायक एवं अत्यन्त मधुर हैं, इसलिए इन्द्रदेब की प्रसन्‍नता के लिये आप शुद्ध होकर प्रतिप्ठित हों
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1795)
- **Original**: 693.यस्य ते पीत्वा वृषभो वृषायते5स्य पीत्वा स्वर्विद: । स सुप्रकेतो अभ्यक्रमीदिषो5च्छा बाज नैतश:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1796)
- **Original**: हे सोमदेव ! बलशाली इन्धदेव आपका पान करके अधिक बलशाली हो जाते हैं । आत्मज्ञानो भी आपका पान करके अत्यधिक आनच्दित होते हैं । ऐसे उत्तम ज्ञानी इन्द्रदेव, आपके बल से संग्राप में विजवी अश्व को भाँति, शौघ्रता से शत्रुओं के धन को अपने अधिकार में ले लेते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1797)
- **Original**: 16 सापवेद-संहित्त 394.इन्द्रमच्छ सुता इसे वृषणं यन्तु हरयः। श्रुष्टे जातास इन्दव: स्वर्विंद:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1798)
- **Original**: शीघरता से शोधित हुआ, देदीप्यमान, ज्ञानवर्द्धक, शुद्ध हरिताभ सोमरस, बलशाली इन्द्रदेव को शीघ्र प्राप्त हो
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1799)
- **Original**: है 695.अय॑ भराय सानसिरिद्धाय पवते सुतः। सोमो जैत्रस्थ चेतति यथा विदे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1800)
- **Original**: युद्ध के समय सेवन योग्य यह सोमरस इन्द्रदेव के लिए तैयार किया जाता है । जैसा कि सभी जानते हैं, विजय के लिए इच्छुक इन्रदेव को यह सोमरस विशेष स्फूर्ति देता है
- **Translation**: 

---

