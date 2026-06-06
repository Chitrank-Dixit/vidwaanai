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

### Verse 1 (Sama Ved 0.1921)
- **Original**: 739.प्र ते अश्नोतु कुक्ष्यो: प्रेन्द ब्रह्मणा शिर:। प्र बाहू शूर राधसा
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1922)
- **Original**: हे इन्द्रदेव ! आफके दोनों पाश्वों में वह सोम भली-भाँति रम जाए । स्तुति के प्रभाव से वह आपके समस्त शरीर में संचरित हो । हे वीर इन्द्र ! ऐश्वर्य प्रदान करने के लिए आपकी भुजाएँ भी समर्थ हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1923)
- **Original**: 740.,आ त्वेता नि षीदतेन्द्रमभि प्र गायत । सखाय स्तोमवाहस:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1924)
- **Original**: हे याज्जिको ! इन्द्रदेव को प्रसन्‍त करने के लिए प्रार्थना करने हेतु शीघ्र आकर बैठो और स्तवन करो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1925)
- **Original**: श्र्ड सामवेद-संहिता 7491.पुरूतम॑ पुरूणामीशान वार्याणाम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1926)
- **Original**: इद्ध॑ सोमे सचा सुते
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1927)
- **Original**: एकत्रित होकर, संयुकतरूप से सोमयज्ञ में शत्रुओं को पराजित करने वाले ऐश्वर्य के स्वामी इन्द्रदेव की अभ्यर्थना करो
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1928)
- **Original**: 742.स घा नो योग आ भुवत्स राये स पुरन्ध्या । गमद्वाजेभिरा स न:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1929)
- **Original**: वे इन््रदेव हमारे पुरुषार्थ को प्रखर बनाने में सहायक हों, हमें धन-धान्य से परिषूर्ण करें, ज्ञानप्राप्ति का मार्ग प्रशस्त करते हुए पोषक अन्न सहित हमारे निकट आएँ
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1930)
- **Original**: 743.योगेयोगे तबस्तरं वाजेवाजे हवामहे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1931)
- **Original**: सखाय इन्द्रमूतये
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1932)
- **Original**: हे #%त्विजो ! सत्कर्मों के शुभारम्भ में, हर प्रकार के संग्राम में, संरक्षण के लिए बलशाली इन्द्रदेव का हम आवाहन करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1933)
- **Original**: 7 / 744. अनु प्रत्मस्यौकसो हुवे तुविप्रर्ति नरम्‌। य॑ ते पूर्व पिता हुवे
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1934)
- **Original**: स्वर्गधाम के वासी, बहुतों के पास पहुँचकर, उन्हें नेतृत्व प्रदान करने वाले इद्धदेव का हम सहायता के लिए आवाहन करते हैं । हमारे पिता ने भी ऐसा ही किया था
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1935)
- **Original**: 745. आ घा गमद्यदि श्रवत्सहस्रिणीभिरूतिभि: । वाजेभिरुप नो हवम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1936)
- **Original**: हमारी प्रार्थना से प्रसन होकर वे इन्द्रदेव निश्चित ही सहस््रों रक्षा-साथनों तथा अन्न-ऐश्वर्य आदि सहित हमारे पास आयेंगे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1937)
- **Original**: 746.इन्द्र सुतेषु सोमेषु क्रतुं पुनीष उक्थ्यम्‌ ।विदे वृधस्य दक्षस्य महाँ हि घ:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1938)
- **Original**: हे इन्द्रदेव ! महान्‌ बल प्राप्ति के लिए सोमरस तैयार करके, किये जाने वाले यज्ञ एवं स्तोत्रों को आप पवित्र करते हैं। आप महान्‌ हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1939)
- **Original**: 747.स प्रथमे व्योमनि देवानां सदने वृश्: । सुपार: सुश्रवस्तम: समप्सुजित्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1940)
- **Original**: साथकों को प्रगति देने वाले, कष्टों से भलीप्रकार त्राण देने वाले, श्रेष्ठ यशदाता, असुरजयी वे इन्द्रदेव, उच्च आकाश में, देवों के आवास में रहते है । हम उनका आवाहन करते हैं
- **Translation**: 

---

