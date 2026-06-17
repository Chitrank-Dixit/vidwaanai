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

### Verse 1 (Vishnu Puran 0.4441)
- **Original**: हुआ बोसस्‍्नगर नामक एक अति रमणीक और सपृद्धि- सम्पन्न नगर था। 6
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4442)
- **Original**: हे पार्थिवोत्तम ! रम्य उपबनोंसे सुझ्ोभित उस पुरपें पूर्वकारूपें ऋभुका शिष्य योगवेत्ता निदाघ रहता था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4443)
- **Original**: महर्षि ऋभु अपने शिष्य निदाघको देखनेके लिये एक सहस््र दिव्यवर्ष बीतनेपर उस नगरपें गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4444)
- **Original**: जिस समय निदाघ बलिखैश्वदेखके अनन्तर अपने द्वारपर ([अतिथियोंकी] प्रतीक्षा कर रहा था, वे उसके दृष्टिगोचर हुए और छह उन्हें द्वारपर पहुँच अर्च्यदानपूर्वक अपने घरमें छे गया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4445)
- **Original**: उस द्विजश्रेष्ठने उनके हाथ-पैर धुलाये और फिर आसनपर बिठाकर आटरपूर्वक कहा--“ भोजन कीजिये'
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4446)
- **Original**: ऋशभु खोले--हे विप्रत़र ! आपके यहाँ क्या-क्या अन्न भोजन करना होगा--यह बताइये, क्योंकि कुत्सित अन्नमें मेरी रुचि नहीं है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4447)
- **Original**: निदाघने कहा--हे द्विजश्रेष्ठ ! मेरे घरमें सत्तू , जौकी रप्सों, कन्द-मूल्ठ-फल्जदि तथा पूए बने हैं। आफ्कों इनमेंसे जो कुक रुचे वही भोजन क्वीजिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4448)
- **Original**: ऋशभु बोल्े--हे द्विज ! ये तो सभी कुत्सित अन्न हैं, मुझे तो तुम हल्ूखा, खीर तथा मड्भा और खाँड़से बने स्वादिष्ट भोजन कराओ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4449)
- **Original**: 8 रचतचतकइछ&$&£$£& अशभीविष्युपुरण _ #####$£ 15 श्रीविष्णुपुराण ( आ* 157 निदाघ उवाच तब निदाघने [ अपनी ख्वीसे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4450)
- **Original**: कहां है हे शालिनि मढ़ेहे यत्किज्लिदतिशों भनम्‌ । शूहदेखि ! हमारे घरगें जो अचछगी-से-अच्छी यस्तु हो उसीसे भ्रष्योपसाधन मृष्टं तेनास्थान्न॑ प्रसाधय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4451)
- **Original**: के लिये अति स्वादि्ट भोजन बताओ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4452)
- **Original**: आम उन ब्राह्मण (जड़भरत ) ने कहा-- उसके ऐसा कहनेपर दर उसकी पत्नीने अपने पतिकोा आज्ञासे उन बिप्रवरके लि इत्युक्ता तेन सा पत्नी मृष्टमन्न॑ द्विजस्य यत्‌।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4453)
- **Original**: आंत स्वादिष्ट अन्न तैयार क्रिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4454)
- **Original**: प्रसाधितवती तह. भर्तुर्वजनगौरवात्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4455)
- **Original**: 15 त॑ भुक्तवन्तमिच्छातो मृष्टमन्न॑ महामुनिम्‌। निदाघः प्राह भूपाल प्रश्रवावनतः स्थित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4456)
- **Original**: 16 निदाघ उवाउ अपि ते परमा तृप्तिरुत्यन्ना तुष्टिरव थे । अपि ते मानस स्वस्थमाहारेण कृत द्विज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4457)
- **Original**: क्व निवासो भवान्विप्र क्व च गन्तुं समुद्यतः । आगम्पते चर भवता यतस्तच्च द्विजोच्यताम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4458)
- **Original**: 18 ऋपुर््वाच क्षुद्यस्थ तस्य भुक्तेउन्ने तृप्तिब्राह्माण जायते । न मे क्षुत्राभवत्तृप्ति: कस्मान्पां परिपृष्छसि
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4459)
- **Original**: 19 वहिना पार्थिते धातौ क्षपिते क्षुत्समुद्धवः । भ्रवत्यभ्मप्ति च क्षीणे नृणां तृडपि जायते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4460)
- **Original**: 20 क्षुत्ृष्णे देहधर्माख्ये न मपैते यतो द्विज । ततः क्षुत्सम्भवाभावात्तृप्तिसस्थेव मे सदा
- **Translation**: 

---

