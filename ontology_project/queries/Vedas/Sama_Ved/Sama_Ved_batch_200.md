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

### Verse 1 (Sama Ved 0.3981)
- **Original**: 1558-साद्ठान्विश्वा अभियुज: क्रतुर्देवानाममृक्तः । अग्निस्तुविश्रवस्तम:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3982)
- **Original**: आक्रामक शत्रु-सेनाओं को परास्त करने वाले, दिव्य गुणों के संवर्द्धक है अग्निदेव ! आप प्रचुर अन्न (पोषण) प्रदान करने वाले हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3983)
- **Original**: 1559. भद्रो नो अग्निराहुतो भद्रा राति: सुभग भद्रो अध्वर:। भद्रा उत प्रशस्तयः:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3984)
- **Original**: आहुतियों से संतुष्ट अग्निदेव हमारे हितैषी हों । हे सौभाग्यशाली अग्निदेव ! आपके कल्याणकारी अनुदान हमें मिलें । हमारे द्वारा सम्पन्न यज्ञ और गान की गई स्तुतियाँ, हमारे लिए मंगलमय हों
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3985)
- **Original**: 1560. भद्रं मनः कृणुष्व वृत्रतूर्ये येना समत्सु सासहिः । अब स्थिरा तनुहि भूरि शर्धतां वनेमा ते अभिष्टये
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3986)
- **Original**: है अग्निदेव ! जीवन-संग्राम में हमें कल्याणकारी विचार प्रदान करें, जिससे पाप पूर्ण विचारों को दबाया जा सके, (उसी से) कामक्रोधादि शत्रुओं को भी नष्ट करें । हम अपने (समग्र) कल्याण के लिए आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3987)
- **Original**: 1561.अग्ने वाजस्थ गोमत ईशान: सहसो यहो । अस्मे देहि जातवेदो महि श्रव:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3988)
- **Original**: हे शक्ति सम्पन्न अग्विदेव ! गवादि पशुओं के साथ उत्पन्न अन्न के आप स्वामी हैं । हे सर्वज्ञाता अग्निदेव ! आप हमें असंख्य ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3989)
- **Original**: 1562.स इधानो वसुष्कविरग्निरीडेन्यों गिरा । रेवदस्मभ्यं पुर्वणीक दीदिहि
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3990)
- **Original**: देदीप्यमान, सभी को वास प्रदान करने वाले (आवास योग्य) वे अम्निदेव ज्ञानयुक्त वाणी से स्तवन योग्य हैं। है जाज्वल्यमान आंग्नदेव ! आप हमें दीप्तियुक्त सम्पदा प्रदान करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3991)
- **Original**: 1563. क्षपो राजन्नुत त्मनाग्ने वस्तोरुतोषसः । स तिग्मजम्भ रक्षसों दह प्रति
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3992)
- **Original**: हे दीप्तिमान्‌ अग्निदेव ! आप सभी दिन-रात्रियों (प्रत्येक क्षण) में दुष्टों को पोड़ित करें और स्वयमेव तेजमुख वाले हे अग्निदिव ! आप असुरों को समूल नष्ट कर दें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3993)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3994)
- **Original**: उत्तराचिके पञ्चदशो5 ध्यायः 15.5
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3995)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3996)
- **Original**: 1564.विशोविशो वो अतिथिं वाजयन्त: पुरुप्रियम्‌ । अग्नि वो दुर्य॑ बच स्तुषे शूषस्य मन्मभि:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3997)
- **Original**: ; अन्न व बल की कामना से युक्त हे याजको ! आप हरेक मनुष्य के गृह में अतिथि रूप में आदरणीय और सर्वप्रिय, अग्निदेव को ह॒विष्य प्रदान करो । आपके बलवर्द्धक स्तवनों से स्थण्डिल (यज्ञवेदी में विद्यमान) अग्नि की हम प्रार्थना करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3998)
- **Original**: 1565.यं जनासो हविष्मन्तो मित्र न सर्पिरासुतिम्‌। प्रशंसन्ति प्रशस्तिभि:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3999)
- **Original**: ह॒विदाता मित्र के समान घृतादि से यज्ञ सम्पन्न करते हुए वैदिक स्तोत्रों से हम पूजनीय अग्निदेव का स्तवन करते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4000)
- **Original**: 1566.पन्‍्यांसं जातवेदसं यो देवतात्युद्यता । हव्यान्यैरयद्धिवि
- **Translation**: 

---

