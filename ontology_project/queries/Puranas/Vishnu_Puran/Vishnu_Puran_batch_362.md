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

### Verse 1 (Vishnu Puran 0.7221)
- **Original**: 2858 श्रीविष्णुपुराण ( आ0“ 6 कुमार॑ चायुषमस्मै चोर्वशी ददौ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7222)
- **Original**: दत्त्वा चैकां निश्ञां तेन राज्ञा सहोषित्वा पश् पुत्रोत्पत्तये गर्भमवाप
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7223)
- **Original**: उवबाचैन राजानमस्मत्ीत्या महाराजाय सर्व एव गन्धर्वा वरदास्संक्‍ृत्ता ब्रियतां च बर इृति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7224)
- **Original**: आह च राजा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7225)
- **Original**: विजितसकलाराति- गन्धवा राज्ञेउप्रिस्थाली. ददु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7226)
- **Original**: ऊचुऔनमप्रिमाप्नायानुसारी भूत्वा. त्रिधा कृत्वोर्वशीसत्केकतामनोर धपुदिए्य सम्यग्यजे था: ततो5बइ्यमभिलषितमवाप्स्यसीस्युक्तस्तामभि- स्थालीमादाय जगाम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7227)
- **Original**: अम्तरटव्यामचिन्तयत्‌ ,अहो मे3तील मूछता किमहमकरवम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7228)
- **Original**: वहिस्थाली मयैषानीता नोर्वश्ीति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7229)
- **Original**: अथैनामटव्यामेवाश्रिस्थालीं तत्याज स्वपुर॑ च जगाम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7230)
- **Original**: व्यतीते<र्द्धरात्रे विनिद्रश्चाचिन्तयत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7231)
- **Original**: मपोर्वशी- साल्तरेक्यप्राप्यर्थमभ्रिस्थाली गन्धर्वैर्दता सा च मयाटव्यां. परित्यक्ता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7232)
- **Original**: तदह तत्र तदाहरणाययास्यामीत्युत्थाय तन्राप्युपगतो नाभिस्थालीमपइ्यत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7233)
- **Original**: शमीगर्भ चाश्वत्थमग्रिस्थालीस्थाने दृष्ठाचित्तयत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7234)
- **Original**: मयात्राभिस्थाली निश्षिप्ता सा चाश्रत्थइशमीगर्भो5भूत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7235)
- **Original**: तदेनमेवाह- मग्रिरूपमादाय स्वपुरमभिगम्यारणी कृत्वा तदुत्पन्नाभेरुपास्ति करिष्यामीति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7236)
- **Original**: एबम्रेव स्वपुरमभिगम्यारणिं चकार
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7237)
- **Original**: तत्पमाणं चाबुलै: कुर्वन्‌ गायत्रीमपठत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7238)
- **Original**: उस समय उर्वशीने उन्हें 'आयु' नामक एक बालक दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7239)
- **Original**: तथा उनके साथ एक रात रहकर पाँच पत्र उत्पन्न करनेके लिये गर्भ धारण किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7240)
- **Original**: और कहा--'हमारे पारस्परिक स्लेहके कारण सकछ गश्धर्वगण महाराजको वरदान देना चाहते हैं अतः आप अधीष्ट वर पाँगिये
- **Translation**: 

---

