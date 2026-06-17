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

### Verse 1 (Sama Ved 0.281)
- **Original**: 991, सोम॑ राजानं वरुणमग्निमन्वारभामहे । आदित्य॑ विष्णुं सूर्य॑ ब्रह्माणं च बृहस्पतिम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.282)
- **Original**: हम (स्तोतागण) , श्रेष्ठ स्तुति के माध्यम से राजा सोम, वरुण, अग्नि, आदित्य, सूर्य, बरह्मणस्पति, विष्णु और बृहस्पति का आवाहन करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.283)
- **Original**: 92. इत एत उदारुहन्दिवः पृष्ठान्या रुहन्‌। प्र भूर्जयो यथा पथोद्ट्यामड्रिसो ययुः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.284)
- **Original**: अंगिरस्‌ ऋषि ने श्रेष्ठ यज्ञ के प्रभाव से च्युलोक की प्राप्ति की और (उसी प्रभाव से) उसके ऊपर (भी) अवस्थित (प्रतिष्ठित) हो गये
- **Translation**: 

---

### Verse 5 (Sama Ved 0.285)
- **Original**: 93. राये अग्ने महे त्वा दानाय समिधीमहि। ईडिष्वा हि महे वृष द्यावा होत्राय पृथिवी
- **Translation**: 

---

### Verse 6 (Sama Ved 0.286)
- **Original**: हे,अग्ते ! महान्‌ ऐश्वर्य देने के लिए हम आपको समिधाओं से प्रदीप्त करते हैं । (याजको) महान्‌ (प्रकृति में चल रहे) यज्ञ के लिए पृथ्वी एवं चुलोक की स्तुति करो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.287)
- **Original**: 94. दघ्न्वे वा यदीमनु वोचदब्रहोति वेरु तत्‌। परि विश्वानि काव्या नेमिश्चक्रमिवा भुवत्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.288)
- **Original**: चक्र (पहिया) को धारण करने वाली धुरी के समान, सम्पूर्ण काव्यों (कर्मों ) के ज्ञाता इन अग्निदेव के निभित्त (उनकी प्रसलता के लिए) पाठ करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.289)
- **Original**: 95. प्रत्यग्ने हरसा हरः श्रृणाहि विश्वतस्परि। यातुधानस्थ रक्षसो बल॑ न्युब्जवीर्यम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.290)
- **Original**: अपने तेज (पराक्रम) से आततायों असुरों (दृष्टों) को नष्ट करने वाले हे अग्ने ! इन असुरों के बल एवं पराक्रम को आप पूर्णतया विनष्ट कर दें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.291)
- **Original**: श््श्ड सापवेट-संहिता 96. त्वमग्ने वसूरिह रुद्रां आदित्याँ उत । यजा स्वध्वरं जन॑ मनुजातं घृतप्रुषम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.292)
- **Original**: वसु , रुद्र और आदित्य (आदि) देवताओं (की प्रसन्नता) के निमित्त यज्ञ करने बाले हे अग्निदेष ! आप घृताहुति से श्रेष्ठ यज्ञ सम्पन्न करने वाले मनु सन्तानों (मनुष्यों) का (अनुदानादि द्वारा) सत्कार करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.293)
- **Original**: इति दशम: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.294)
- **Original**: एकादशः खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.295)
- **Original**: 97. पुरु त्या दाशिवाँ बोचे5रिरग्ने तव स्विदा । तोदस्थेव शरण आ महस्य
- **Translation**: 

---

### Verse 16 (Sama Ved 0.296)
- **Original**: महान्‌ सम्पत्तिशाली की शरण में आये हुए, (धन-याचक) सेवक के सदश, हम अग्निदेव के निमित्त आहुति प्रदान करते हुए , स्तुतिगान करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.297)
- **Original**: 98. प्र होत्रे पूर््य॑ बचो5ग्नये भरता यृहत्‌। विपां ज्योतीर्षि बिश्रते न वेधसे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.298)
- **Original**: हे स्तोताओ ! तत्त्वज्ञानियों के तेज को धारण करने वाले, विधाता आदि देवों का आवाहन करने वाले, अग्निदेव की श्रेष्ठ एवं प्राचीन स्तोत्रों से स्तुति करो
- **Translation**: 

---

### Verse 19 (Sama Ved 0.299)
- **Original**: 99. अग्ने वाजस्थ गोमत ईशानः सहसो यहो । अस्मे देहि जातवेदो महि श्रव:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.300)
- **Original**: (अरणिमन्थन रूप) बल से उत्पन हुए, ज्ञान को उत्पन्न करने वाले एवं गौओं से उत्पन्न अन्ग (पोषक पदार्थों) के अधिपति हे अग्ने ! आप हमें प्रभूत धन-वै भव प्रदान करें
- **Translation**: 

---

