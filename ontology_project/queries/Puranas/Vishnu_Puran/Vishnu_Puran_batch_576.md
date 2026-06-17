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

### Verse 1 (Vishnu Puran 0.11501)
- **Original**: तत्कध्यतां महाभाग यदन्यत्कृतवान्बलः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11502)
- **Original**: अीपराशर उवाच मैत्रेय श्रूयतां कर्म यद्रामेणाभवत्कृतम्‌। अनन्तेनाप्रमेबेन शेषेण. धरणीथृता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11503)
- **Original**: सुयोधनस्थ तनयां स्वयंबरकृतक्षणाम्‌ । बलादादत्तवान्वीरस्साम्बो जाम्बवतीसुतः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11504)
- **Original**: ततः क्रुद्धा महावीर्या: कर्णदुर्योधनादब: । भीष्पद्रोणादयश्ैन॑ बबन्धुर्युधि निर्जितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11505)
- **Original**: तच्छुत्वा यादवास्सवें क्रोध दुर्योधनादिषु । पैत्रेय चक्कुः कृष्णश्ष ताब्रिहन्तुं महोद्यमम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11506)
- **Original**: तान्षिवार्य बल: प्राह मदल्लोलकलाक्षरम्‌। मोक्ष्यन्ति ते मद्गचनाद्यास्याम्येको हि कौरवान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11507)
- **Original**: अीपयरशार ठवाच बलदेवस्ततो गत्वा नगर नागसाह्यम्‌। बाह्योपवनमध्ये5भून्न विवेश च तत्पुरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11508)
- **Original**: बल्मागतमाज्ञाय भूषा दुर्योधनादव: । गामर्घ्यमुद्क॑े चैब रामाय प्रत्यवेदयन्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11509)
- **Original**: श्रीमैश्रेयजी खोले--हे ब़रहान्‌! अब मैं फिर मतिमान्‌ बलभद्गजीके पराक्रमकी वार्ता सुनना चाहता हूँ, वर्णन कीजिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11510)
- **Original**: हे भगवन्‌ ! मैंने उनके यमुनाकर्षणादि पराक्रम तो सुन लिये; अब है महाभाग ! उन्होंने जो और-और विक्रम दिखत्खये हैं उनका वर्णन कोजिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11511)
- **Original**: श्रीपराशरजी बोले--हे मैत्रेय ! अनन्त, अप्रमेय घरणीधर चोषावतार श्रीबलरामजीने जो कर्म किये थे, वह सुनो--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11512)
- **Original**: एक बार जाम्बवती-ननन्‍्दन वीरवर साम्बने स्वयैवरके अवसरपर दुर्योधनकी पुत्रीको बत्मत्‌ हरण किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11513)
- **Original**: तब महावीर कर्ण, दुर्योधन, भीष्प और द्रोण आदिने क्रुद्ध होकर उसे युद्धमें हराकर नाँध लिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11514)
- **Original**: यह समाचार पाकर कृष्णचन्द्र आदि समस्त यादबोंने दुर्योधनादिपर क्रुद होकर उन्हें मारनेके लिये बड़ी तैयारी की
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11515)
- **Original**: उनको रोककर श्रीबलरामजीने मदिराफे उन्पादसे लड़खड़ाते हुए शब्दोंमें कहा--'“कौरवगण मेरे कहनेसे साम्बको छोड़ देंगे अतः मैं अकेल्त्र ही उनके पास जाता हूँ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11516)
- **Original**: श्रीपराधारजी बोले--तदनन्तर, श्रीबल्देवजी हस्तिनापुरके समीप पहुँचकर उसके बाहर एक उच्चानमें ठहर गये; उन्होंने नगरमें प्रवेश नहीं किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11517)
- **Original**: बलरामजीको आये जान दुर्योधन आदि ग़ाजाओंने उन्हें गौ, अर्घ्य और पाद्यादि निवेदन किये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11518)
- **Original**: ड06 श्रीविष्णुपुराण [ अ0 37 गृहीत्वा विधिवस्सर्व ततस्तानाह कौरवान्‌ । उन सबको चिधिवत्‌ ग्रहण कर बलभद्रजीने कौरचोंसे आज्ञापयत्युअसेनस्साम्बमाशु बिमुझ्त
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11519)
- **Original**: कहा--“राजा उपसेनको आज्ञा है आपल्केग साम्बको ततस्तद्वचनं श्रुत्वा भीष्यद्रेणादयों नृषा: । कर्णदुर्योधनाद्याश्चन॒ चुक्षुभुद्विजसत्तम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11520)
- **Original**: 11 ऊचुश्च कुपितास्सवें बाह्लिकाद्याश्न कौरवाः
- **Translation**: 

---

