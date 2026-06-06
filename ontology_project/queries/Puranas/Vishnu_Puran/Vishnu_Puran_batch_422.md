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

### Verse 1 (Vishnu Puran 0.8421)
- **Original**: ते ब्राह्मणा वेदवादानु- बन्धीनि वचांसि राज्यमग्रजेन कर्त्तव्यमित्यर्थबन्ति तमूचु:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8422)
- **Original**: असावपि देबापिवेंद्बादविरोध - युक्तिदूषितमनेकप्रकार॑ तानाह
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8423)
- **Original**: ततस्ते ब्राह्मणाइशान्तनुपूचु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8424)
- **Original**: _ आगच्छ है राजन्नलमतन्नातिनिर्बन्धेन प्रश्ानतत एजासाबनावृष्टि- दोष: पतितोउइयमनादिकालप्हितवेदबचन- दृषणोश्वारणात्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8425)
- **Original**: पतिते चाग्रजे नैव ते परिवितृत्व॑ भवतीत्युक्तश्शान्तनुस्स्खपुरमागम्य राज्यमकरोत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8426)
- **Original**: वेदवादविरों धवचनोच्चारण- दूषिते च तस्मिन्देवापौ तिष्ठत्यपि ज्येष्ठ भ्रार्यखिल- सस्यनिष्पत्तवे खवर्ष भगवान्पर्जन्य:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8427)
- **Original**: थे तथा उनके स्पर्ससे सम्पूर्ण जीब अत्युत्तम ज्ञाक्तिलाभ करते थे, इसलिये वे झाच्तनु कहल्यते थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8428)
- **Original**: एक बार महाराज ज्ञात्तनुके राज्यमें बारह वर्षतक वर्षा न हुई
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8429)
- **Original**: उस समय सम्पूर्ण देशकों नष्ट होता देखकर राजाने ब्राह्मणोंसे पूछा, “हमारे राज्यमें वर्षा क्‍यों नहीं हुई ? इसमें मेरा क्या अपराध है ?"
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8430)
- **Original**: तब ब्राह्मणोंने उससे कहा--'यह ग्रज्य तुम्हारे बड़े भाईका है किंतु इसे तुम भोग रहे हो; इसलिये तुम परियेता हो।' डनके ऐसा कहनेपर राजा शान्तनुने उनसे फिर पूछा, “तो इस सम्बन्धमें मुझे अब क्‍या करना चाहिये ?'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8431)
- **Original**: 16---18
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8432)
- **Original**: इसपर ले ब्राह्मण फिर बोले--'जबतक तुम्हारा बड़ा भाई देवापि किसी प्रकार पतित न हो तबतक यह राज्य उसीके योग्य है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8433)
- **Original**: अतः तुप्त इसे उसोवे दे डालो, तुम्हारा इससे कोई प्रयोजन नहीं ?' ब्राह्मणोंके ऐसा कहनेपर शान्तनुके मन्‍ली अइमसारीने वेदबादके विरुद्ध बोलनेवाले तपस्वियोंको वनमें नियुक्त किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8434)
- **Original**: उन्होंने अतिहाय सरलूमति राजकुमार देवापिकी बुद्धिको बेदवबादके विरुद्ध मार्ममें प्रयत्त कर दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8435)
- **Original**: उधर राजा जान्तनु ब्राह्मणोंके कथनानुसार दुःस्र और शोकयुक्त होकर ब्राह्मणॉकी आगेकर अपने बड़े भाईको राज्य देनेके लिये यनमें गये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8436)
- **Original**: उनमें पहुँचनेपर वे ब्राह्मणगण परम बिनीत राजकुमार देवापिके आश्रमपर डपस्थित हुए; और उससे “ज्येष् भ्राताकों ही राज्य करना चाहिये'--इस अर्थके समर्थक अनेक बेदानुकूल वाक्य कहने छगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8437)
- **Original**: । किन्तु उस सगय देनापिने बेदबादके विरुद्ध नाना प्रकारको युक्तियोंसे दूषित बातें कों। 26
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8438)
- **Original**: तब उन ब्राह्मणोंने झान्तनुसे कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8439)
- **Original**: “हे राजन्‌ ! चल्त्रे, अब यहाँ अधिक आग्रह करनेकी आवश्यकता नहीं। अब अनावृष्टिका दोष शान्तत हो गया। अनादिकालसे पूजित बेदवाक्योंमें दोष बतलानेके कारण देवापि पतित हो गया है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8440)
- **Original**: ज्येष्ट भ्रात्राके पतित हो जानेसे अब तुम परिवेत्ता नही रहे ।'' उनके ऐसा कहनेपर शान्तनु अपनों राजधानीकों चले आये और राज्यशासन करने लगे
- **Translation**: 

---

