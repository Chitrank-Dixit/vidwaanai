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

### Verse 1 (Bramha 0.8801)
- **Original**: महाराज कराल! तुमने मुझसे आज परब्रह्मका प्रकृतिसे सम्बन्ध रखनेपर एकत्व और नानात्वको
- **Translation**: 

---

### Verse 2 (Bramha 0.8802)
- **Original**: ज्ञान प्राप्त किया है। अब तुम्हारे मनमें तनिक भी प्राप्त होता है। प्रलयकालमें तो वह भी एक ही
- **Translation**: 

---

### Verse 3 (Bramha 0.8803)
- **Original**: भय नहीं होना चाहिये। नरेन्द्र! तुमने मुझसे रूपमें रहता है, किंतु सृष्टिके समय प्रकृतिको
- **Translation**: 

---

### Verse 4 (Bramha 0.8804)
- **Original**: जैसा प्रश्न किया था, उसके अनुसार ही मैंने प्रेरित करनेके कारण उसकी ही अनेकतासे वह
- **Translation**: 

---

### Verse 5 (Bramha 0.8805)
- **Original**: तुम्हें यह उपदेश किया है; कोई दूसरी बात नहीं स्वयं भी अनेक-सा प्रतीत होता है। परमात्मा
- **Translation**: 

---

### Verse 6 (Bramha 0.8806)
- **Original**: कही है। यह महान्‌ ज्ञान मोक्षवेत्ता पुरुषोंका ही प्रकृतिको प्रसवके लिये उन्मुख करके उसे
- **Translation**: 

---

### Verse 7 (Bramha 0.8807)
- **Original**: परम आश्रय है। यह मुझे साक्षात्‌ ब्रह्माजीसे प्राप्त अनेक रूपोंमें परिणत करता है। प्रकृति और
- **Translation**: 

---

### Verse 8 (Bramha 0.8808)
- **Original**: हुआ है। उसके विकारोंको क्षेत्र कहते हैं । चौबीस तत्त्वोंस
- **Translation**: 

---

### Verse 9 (Bramha 0.8809)
- **Original**: व्यासजी कहते हैं--मुनिवरो! पूर्बकालमें भिन्‍न जो पच्चीसवाँ तत्त्व महान्‌ आत्मा है, वही
- **Translation**: 

---

### Verse 10 (Bramha 0.8810)
- **Original**: महर्षि वसिष्ठने जिस प्रकार पत्चीसवें तत्त्वरूप उस क्षेत्रमें अधिष्ठातारूपसे निवास करता है।
- **Translation**: 

---

### Verse 11 (Bramha 0.8811)
- **Original**: परब्रह्मके स्वरूपका वर्णन किया था, उसी बह क्षेत्रको जानता है, इसलिये क्षेत्रज्ञ कहलाता
- **Translation**: 

---

### Verse 12 (Bramha 0.8812)
- **Original**: प्रकार मैंने तुम्हें बताया है। यही बह ब्रह्म है, है। क्षेत्रज्ञ प्रकृतिजनित पुर (शरीर)-में शयन
- **Translation**: 

---

### Verse 13 (Bramha 0.8813)
- **Original**: जिसे जान लेनेपर मनुष्य फिर इस संसारमें नहीं करता है, इसलिये उसे पुरुष कहते हैं । वास्तवमें
- **Translation**: 

---

### Verse 14 (Bramha 0.8814)
- **Original**: आता। यह ज्ञान हिरण्यगर्भ ब्रह्माजीसे महर्षि क्षेत्र अन्य वस्तु है और क्षेत्रज्ञ अन्य। क्षेत्र
- **Translation**: 

---

### Verse 15 (Bramha 0.8815)
- **Original**: बसिष्ठको प्राप्त हुआ, वसिष्ठजीसे देवर्षि नारदको अव्यक्त (प्रकृति) है और क्षेत्रज्ञ उसका ज्ञाता
- **Translation**: 

---

### Verse 16 (Bramha 0.8816)
- **Original**: मिला और देवर्षि नारदसे मुझको प्राप्त हुआ। पच्चीसवाँ तत्व परमात्मा है। जब पुरुष अपनेको
- **Translation**: 

---

### Verse 17 (Bramha 0.8817)
- **Original**: वही यह सनातन ज्ञान मैंने तुम सब लोगोंको प्रकृतिसे भिन्‍त्र जान लेता है, उस समय वह
- **Translation**: 

---

### Verse 18 (Bramha 0.8818)
- **Original**: बताया है; यह परम पद है, इसका श्रवण करके अद्वितीय परमात्मरूपसे स्थित होता है। इस
- **Translation**: 

---

### Verse 19 (Bramha 0.8819)
- **Original**: अब तुम्हें शोक नहीं करना चाहिये। जिसने क्षर प्रकार मैंने तुम्हें सम्यग्‌ दर्शन (सांख्य)-का
- **Translation**: 

---

### Verse 20 (Bramha 0.8820)
- **Original**: और अक्षरके भेदको जान लिया, उसे किसी यथार्थ वर्णन किया। जो इसे इस प्रकार जानते
- **Translation**: 

---

