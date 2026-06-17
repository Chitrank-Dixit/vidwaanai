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

### Verse 1 (Vishnu Puran 0.10301)
- **Original**: 9 तामाह ललित कृष्ण: कस्येदमनुलेपनम्‌ । भ्रवत्या नीयते सत्य॑ वदेन्दीवरललोचने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10302)
- **Original**: 2 सकामेनेव सा प्रोक्ता सानुरागा हरि प्रति । प्राह सा ललित कुब्जा तदर्शनबलात्कृता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10303)
- **Original**: 3 कात्त कस्मान्न जानासि कंसेन विनियोजिताम्‌ । नैकबक्रेति. बिख्यातामनुलेपनकर्मणि । 4 नान्यपिष्टं हि कंसस्य प्रीतय्रे ह्नुलेपनम्‌। भवाम्यहमतीवास्य प्रसादधनभाजनम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10304)
- **Original**: 5 श्रीकृष्ण उवाच सुगश्चमेतद्राजाह रुचिरं रुचिरानने । आवयोगांत्रसदृश॑. दीवतापनुलेपनम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10305)
- **Original**: 6 श्रीपराशरजी खोले-- तदनन्तर श्रोकृष्णचन्धने राजमार्गपें एक नवयौवना कुब्जा खत्रीकों अनुछेपनक्ता पात्र लिये आतो देखा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10306)
- **Original**: तब अ्रीकृष्णने उससे विस्थसपूर्वक्ाक कहा--“अयि कमसलल्ओोचने ! तू सच-सच बता यह अनुलेपन किसके ल्प्यि ले जा रही है 2”
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10307)
- **Original**: भगवान्‌ कृष्णके क्मुक पुरुषकी भाँति इस प्रकार पुछनेपर अनुरागिणी कुब्जाने उनके दर्शनसे हख्रत्‌ आकृष्टचित्त हो अति ललित भावसे इस प्रकार कहा--
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10308)
- **Original**: “हे कान्त ! क्‍या आप मुझे नहीं जानते ? मैं अनेकवक्रा-नामसे विख्यात हूँ, राजा कैसने मुझे अनुलेपन-कार्यमें नियुक्त किया है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10309)
- **Original**: राजा कंसको मेरे अतिरिक्त और किसीका पीसा हुआ उबटन पसन्द नहीं है, अतः मैं उनकी अत्यन्त कृपापात्री हूँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10310)
- **Original**: श्रीकृष्णजी बोले--हे सुमुख्ति! यह सुन्दर सुगन्धमय अनुछेपन तो राजाके ही योग्य है, हमारे दारीरके योग्य भी कोई अनुकेषन हो तो दो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10311)
- **Original**: आः 20 ] श्रीपराझर उबाच श्रु्वैतदाह सा कुब्जा गृह्मयतामिति सादरम्‌। अनुलेपन चर प्रददौ गात्रयोग्यमओोभयो:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10312)
- **Original**: 7 भक्तिच्छेदानुलिप्ताड्डी ततस्तौ पुरुषर्षभो । सेन्द्रचापौ व्यराजेतां सितकृष्णाविबाम्बुदो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10313)
- **Original**: 8 ततर््ता चिब्रुके झौरिस्ल्कापनविधानवित्‌ । उत्पाट्य तोलयामास इबब्लुलेनाप्रषाणिना
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10314)
- **Original**: 9 चकर्ष पदृभ्यां च तदा ऋजुत्व॑ केशवो5नयत्‌ । ततस्सा ऋजुतां प्राप्ता योषितामभवद्वरा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10315)
- **Original**: 90 विलासललितं प्राह प्रेमगर्भभरालसप्‌ । बच्े प्रगृह्य गोविन्द मम गेहं व्रजेति वै
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10316)
- **Original**: 11 एवपुक्तस्तया झौरी रामस्थालोक्य चाननम्‌ । प्रहस्य कुब्जां तामाह नैकवक्रामनिन्दिताम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10317)
- **Original**: 12 आयास्थे भव॒तीगेहमिति तां प्रहसन्हारि: । विससर्ज जहासोच रामस्यात्लोक्य चाननम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10318)
- **Original**: 13 भक्तिभेदानुलिप्ताड़ों नीलपीताम्बरो तु तो । धनुश्शाल्ां ततो यातौ चित्रमाल्योपशोभितो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10319)
- **Original**: 14 आयागं तद्धनूरत्न॑ ताभ्यां पृष्टेस्तु रक्षिभि: । आख्याते सहसा कृष्णो गृहीत्वापूरयद्धनु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10320)
- **Original**: 15 ततः पूरयता तेन भज्यमानं बलाद्धनुः । चकार सुमहच्छब्दं॑ मथुरा येन पूरिता
- **Translation**: 

---

