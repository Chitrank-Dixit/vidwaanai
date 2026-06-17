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

### Verse 1 (Vaivtpuran 15.19239)
- **Original**: त्वं बुद्धेर्जेननी मातः को वा त्वां स्तोतुमीश्ररः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.19240)
- **Original**: यद्वस्तु दृष्ट सर्वेषां तद्दियक्तुं बुध: क्षम:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.19241)
- **Original**: यददृष्टाश्रुत॑ वस्तु तत्रिर्वक्तु. च कः शक्षम:ः। अहं महेशो5नन्तश्न स्तोतुं त्वां कोउपि न क्षम:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.19242)
- **Original**: सरस्वती चर वेदाश्न क्षमः कः स्तोतुमीश्ररि । यथागर्म यथोक्ते चर न मां निन्दितु्मनईसि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.19243)
- **Original**: ईश्वराणामी श्वरस्प योग्यायोग्ये समा कृपा । जनस्य प्रतिपाल्यस्थ क्षण दोष: क्षणे गुण:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.19244)
- **Original**: जननी जनको यो वा सर्ब क्षमति स्नेहतः । इत्युक्त्थां जगतां धाता तस्थौं च॑ पुरतस्तयो:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.19245)
- **Original**: प्रणम्य चरणाम्भोज॑सर्वेषां बन्द्ामीप्सितम्‌ । ब्रहाणा च॒ कृतं स्तोत्र त्रिसंध्य॑ यः पठेन्नर:। राधामाथवयो: पादे भक्ति दास्य॑ लभेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.19246)
- **Original**: कर्मनिर्मूलन॑ कृत्वा मृत्युं जित्वा सुदुर्जयम्‌ । विलछ्ुधय सर्वलोकांश्व याति गोलोकमुत्तमम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.19247)
- **Original**: इति तब्रह्मवैवर्ते ब्रह्मणा कृतं औरधास्तोत्र सम्पूर्णम्‌ । ( श्रीकृष्णजन्मखण्ड 15
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.19248)
- **Original**: 94--116) 28038 लक. 4050050070 श्रीनारायणकृतं राधाषोडशनामवर्णनम्‌ श्रीनारायण उवाच राधा रासेश्वरी रासवासिनी रसिकेश्वरी । कृष्णप्राणाधिका कृष्णप्रिया कृष्णस्वरूपिणी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.19249)
- **Original**: कृष्णबामाड्ुसम्भूता परमानन्दरूपिणी । कृष्णा बृन्दावनी बृन्दा बृन्दाबनविनोदिनी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.19250)
- **Original**: अन्द्रावली. अन्द्रकान्ना शतचन्द्रप्रभानना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.19251)
- **Original**: नामान्येतानि साराणि तेषामभ्यन्तराणि च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.19252)
- **Original**: राधेत्येब॑ च्ञ संसिद्धौ राकारों दानवाचक:। स्वयं निर्वाणदात्री या सा राधा परिकीर्तिता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.19253)
- **Original**: रासेश्वरस्थ पलीय॑। तेन रासेश्वरी स्मृता। रासे च वासों यस्याश्च तेन सा रासवासिनी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.19254)
- **Original**: सर्वासां रसिकानां च॒ देवीनामीश्वरी परा। प्रवदन्ति पुरा सनन्‍्तस्तेन तां रसिकेश्वरीम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.19255)
- **Original**: प्राणाधिका प्रेयसी सा कृष्णस्यथ परमात्मनः । कृष्णप्राणाधिका सा च कृष्णेन परिकीर्तिता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.19256)
- **Original**: कृष्णस्थातिप्रिया कान्ता कृष्णो वास्या: प्रिय: सदा । सर्वैर्देवगणैरक्ता तेन कृष्णप्रिया स्मृता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.19257)
- **Original**: कृष्णरूपं संनिधातुं या शक्ता चावलीलया । सर्वाशै: कृष्णसद्शी तेन कृष्णस्वरूपिणी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.19258)
- **Original**: वामाड़ार्धेन कृष्णस्थ या सम्भूता परा सती
- **Translation**: 

---

