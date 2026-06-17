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

### Verse 1 (Vishnu Puran 0.7781)
- **Original**: न इ्वनुल्लदूघ्य वरपादपं तत्कृत- नीडाश्रयिणो विह्डमा वध्यन्ते तदलममुनास्मत्पुरतः शोकप्रेरितवाक्यपरिकरेणेत्युक्वा. द्वारका- मभ्येत्येकान्ते बलदेवे वासुदेव: प्राह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7782)
- **Original**: सृगयागतं प्रसेनमटव्यां मृगपतिर्जघान
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7783)
- **Original**: सत्राजिदप्यधुना शतधन्वना निधन .प्रापित:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7784)
- **Original**: तदुभयविनाझात्तत्मणिरत्रमावाभ्यां सामान्य भविष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7785)
- **Original**: तदुत्तिष्ठारुह्मतां रथः शतघन्वनिधनायोद्यम॑. कुर्वित्यभिहितस्तथेति समन्वरीप्सितवान्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7786)
- **Original**: । कृतोद्ममौ च तावुभावुपलभ्यशतधन्वा कृतवर्माणमुपेत्य पाष्णिपूरणकर्मनिषित्तमचोदयत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7787)
- **Original**: आह चेन॑ कृतवर्मा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7788)
- **Original**: नाहें बलदेववासुदेवाभ्यां सह विरोधायालमित्युक्त- श्वाक़ूरमनोक्यत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7789)
- **Original**: असावप्याह
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7790)
- **Original**: पकर्षणाविकृतमहिमोरुसीरिण सीरिणा सच सह सकलजगहइलन्झानाममस्वराणामपि योद्धु समर्थ: किमुताहम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7791)
- **Original**: तदन्यइशरण- चतुर्थ अंग 275 उनके चले जानेपर शतथन्वाने सोते हुए सत्राजितक्ते मास्कर वह मणिरल्न छे स्त्या
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7792)
- **Original**: पिताके वधसे क्रोधित हुई सत्यभामा तुरन्त ही रथपर चढ़कर गारणाबतत नगरमें पहुँचों और भगजान्‌ कृष्णसे बोली, 'भगवन्‌ ! पिताजीने मुझे आपके करकमलोंपिं सौंप दिया--इस बातकों सहन न कर सकनेके कारण शतघन्चाने मेरे चिताजीको मार दिया है और उस स्थमनन्‍्तक नापक मणिरत्रको ले लिया है जिसके प्रय्पशसे सम्पूर्ण त्रिल्‍्लेकी भी अखकारशून्य हो जायगीं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7793)
- **Original**: इसमें आपहीकी हैसी है इसर्ल्यि सब यातोंका विचार करके जैसा डचित समझें, करें"
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7794)
- **Original**: सत्यभामाके ऐसा कहनेपर भगलान्‌ श्रीकृष्णने मन-ही-मन प्रसन्न होनेपर भी उनसे क्रोधसे आँखें लाल करके कहा--+
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7795)
- **Original**: 'सत्ये ! अवश्य इसमें मेरो ही हँसी है, उस दुरात्पाके इस कुकर्मको मैं सहन नहीं कर सकता, क्योंकि यदि ऊँचे वृक्षका उल्लड्भून न किया जा सके तो उसपर घोंसला बनाकर रहनेवाए्े पक्षियोंको नहीं मार दिया जाता [ अर्थात्‌ बडे आदमियोंसे पार न पानेपर उनके आश्वितोंकों नहीं दकवाना चाहिये। ] इसलिये अब तुम्हें हमारे सामने इन शोक-प्रेरित याययोके कहनेकी और आवदयकता नहीं है।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7796)
- **Original**: तुम शोक र्त्रेड़ दो, मैं इसका भली प्रकार बदल्म चुका दूँगा।
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7797)
- **Original**: " सत्यभामासे इस प्रकार कह भगवान्‌ तासुदेषने द्वारकामें आकर श्रीबलदेवजीसे एकान्तमें कहा---
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7798)
- **Original**: “वनमें आखेटके र्थये गये हुए प्रसेनक्रो तो सिंहने सार दिया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7799)
- **Original**: अब हातघन्याने सन्राजितूको भी मार दिया है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7800)
- **Original**: इस प्रकार उन दोनोंके मारे जानेपर मणिरल स्थमन्तकपर हम दोनोंका समान अधिकार होगा । 49
- **Translation**: 

---

