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

### Verse 1 (Sama Ved 0.2341)
- **Original**: हे मतिमान्‌ सोमदेव ! आप अपनी प्रिय सरसधार सहित शीघ्र ही उपस्थित हों । जहाँ देवताओं का निवास है, वहाँ (यज्ञीय वातावरण में) आप पधारें, ऐसा हमारा आग्रह है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2342)
- **Original**: 899.परिष्कृण्वन्ननिष्कृतं जनाय यातयन्निष: । वृष्टिं दिवः परि स्नरव
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2343)
- **Original**: हे सोमदेव ! संस्काररहित क्षेत्र को संस्कारवान्‌ बनाते हुए, मानवमात्र के निभित्त अन्न आदि उत्पन्न करने के लिए आप आकाश से वर्षा करें । (प्राण-पर्जन्य के रूप में आपका अनुग्रह जल के साथ प्राप्त हो ))
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2344)
- **Original**: 900.अयं॑ स यो दिवस्परि रघुयामा पवित्र आ। सिन्धोरूर्मा व्यक्षरत्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2345)
- **Original**: आकाश में मन्दगति से विचरण करने वाला, पवित्र किया जाता हुआ सोमरस, सागर (नदी) जलाशय आदि की लहरों को प्राप्त होता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2346)
- **Original**: 901.सुत एति पवित्र आ त्विषिं दधान ओजसा
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2347)
- **Original**: विचक्षाणो विरोचयन्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2348)
- **Original**: सबका निरीक्षक, सबका प्रकाशक, दिव्य सोम अंतरिक्ष से प्राकृतिक छनने से छनता हुआ तीजगति से अवतरित होता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2349)
- **Original**: उत्तराथिके पश्चमो5 व्याय: 5.3 * 902.आविवासन्परावतो अथो अर्वावतः सुत:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2350)
- **Original**: इन्धाय सिच्यते मधु
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2351)
- **Original**: तैयार किया हुआ सोमरस, दूर एवं समीप से (समुचित रीति से) संस्कारित (पवित्र) करके. इन्द्रदृव को स्रमर्पित किया जाता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2352)
- **Original**: 903.समीचीना अनूषत हरिं हिन्वन्त्यद्रिभि:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2353)
- **Original**: इन्दुमिद्बाय पीतये
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2354)
- **Original**: शिलाओं के द्वारा पीसकर निकाले गये, ताजे हरे रंग वाले सोमरस को, पान करने हेतु, देवराज इद्ध को समर्पित किया जाता हैं ! $ग़् समय एक स्थान पर एकत्रित साधक उनकी स्तूृति करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2355)
- **Original**: 904.हिन्वन्ति सूरमुस्तय: स्वसारों जामयस्पतिम्‌। महामिन्दुं महीयुव:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2356)
- **Original**: । बहिनों की तरह श्षाथ-साध स्नेहपूर्वक रहने वाली, सब जगह पहुँचने वाली अँगुलियाँ, अपने श्रेष्ठ स्वागी स्रोमरस को निकालने का महान्‌ कार्य करती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2357)
- **Original**: 905,पवमान रुचारुचा देव देवे भ्य: सुतः । विश्वा वसून्‍्या विश
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2358)
- **Original**: शुद्ध किये गये हे तेजस्वी सोमदेव ! आप देवताओं को समर्पित करने के लिए तैयार किये गये हैं। सब प्रकार की (सांसारिक एवं दैवी) सम्पदाएँ आप हमें प्रदान को
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2359)
- **Original**: 906.आ पवमान सुष्ट॒ति वृष्टिं देवे भ्यो दुव:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2360)
- **Original**: इृषे पवस्व संयतम्‌
- **Translation**: 

---

