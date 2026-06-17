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

### Verse 1 (Sakand Puran 9.8761)
- **Original**: मन्त्रद। मन्प्रहा। मन्‍्त्री, तन्‍्त्री, कत्रजनपरिय, सन्मत्त्र, मन्त्रवितू: सन्‍्त्री, यन्त्रमन्जेकमझन। सारण, सोहन। मोदी, स्म्भोच्ाट्नक्ृत्‌+ खड भ्रहुमाय, विमाय, महामायाविमोहक
- **Translation**: 

---

### Verse 2 (Sakand Puran 9.8762)
- **Original**: मोक्षदों बसख्चयकों बम्दी द्वाकर्पणविकर्षणः । ड्रीड्वारो बीजरूपी ल कछीजवारः कीरूकाणिपः
- **Translation**: 

---

### Verse 3 (Sakand Puran 9.8763)
- **Original**: सौडझ्शारः शक्तिमाष्छक्ति:ः सर्वशक्तिधरों घरः। अकारोफार ओक्वारश्छल्दों.. गायत्रसस्भवः # मोशद, वस्धक, ब्न्‍्दी, आ#%र्पण, विदूष॑ण+ डीडझ्ार; बीज़रूपी। क्लौक्भार, कीलकाध्रिप, सौक्वार; शक्तिमान्‌, शक्ति; सर्वशक्तिधर, घर, अकार; उक्ार, ऊं>कार+ छन्‍्द, गायत्रसम्भव
- **Translation**: 

---

### Verse 4 (Sakand Puran 9.8764)
- **Original**: वेदों वेदबिद्ों येद्री वेवाध्यायी सदाशिवः । ऋणग्पजञुःसामाथर्वेशः ख्ामगानकरो5करी
- **Translation**: 

---

### Verse 5 (Sakand Puran 9.8765)
- **Original**: 17 जिपदों बहुपादी च॑ सत्पयः सर्वंतोमुणः
- **Translation**: 

---

### Verse 6 (Sakand Puran 9.8766)
- **Original**: प्राकृतः संस्कृतों योगी शीतप्रश्यप्रहेक्तिक:
- **Translation**: 

---

### Verse 7 (Sakand Puran 9.8767)
- **Original**: बेद, वेदबिद, वेदी, वेदाध्यावी, सदाशिव+ अग्यजु।- सामापवेंश। खामगानकर। अकरी। ज़िपद। बहुपादी। सत्पथ+ सर्यतोमुस्तर, प्राकृत, संस्कृत, योगी, गौतप्रत्थप्रदेलिक
- **Translation**: 

---

### Verse 8 (Sakand Puran 9.8768)
- **Original**: सगुणो विगुणइफ़़ल्दो निःसक़ो विगुणों गुणी। निर्युणो गशुलवाल्‌ सजी कर्मी धर्मी चर कर्मंदः # गुणवान्‌, सक्ली। कर्मी, धर्मी, कर्मद, मिल्कर्मा, कामकामी, सर्वंसज़॒कर) रागी। सर्वत्यागी+ यहिआर, एकपाद) दिपाद, बहुपाद, अल्पणदक) द्विपद) जिपद+ पांदी। विषांदी, पदुसंप्रह+ खेचर।, भूचर) आामी; आन्नकीटमधुविव
- **Translation**: 

---

### Verse 9 (Sakand Puran 9.8769)
- **Original**: ऋतुः संचस्सरों मॉसोउ्यन। पक्षों क्ादर्तिसः
- **Translation**: 

---

### Verse 10 (Sakand Puran 9.8770)
- **Original**: कृर्त थ्रेता कसिश्रेय. द्वापरखतुराक॒तिः
- **Translation**: 

---

### Verse 11 (Sakand Puran 9.8771)
- **Original**: वेशकाऊुकर!ः कांछः कुशघर्मी सनांतनः
- **Translation**: 

---

### Verse 12 (Sakand Puran 9.8772)
- **Original**: कुछा काहा पर्ता साकणों थाम पक्ष/ सितासितः
- **Translation**: 

---

### Verse 13 (Sakand Puran 9.8773)
- **Original**: ऋतु, संवत्सर, मास, अयन पक्ष: अर्धर्नित, कृत, ज्रेता। कुष्ठि, द्वापर, चतुराकृति। देशकालकर, काल, सनातन कुछपर्म॑ कला; काप्ठा; फ्लो, नांडी; याम। सितासित, पक्ष
- **Translation**: 

---

### Verse 14 (Sakand Puran 9.8774)
- **Original**: झुगो यशुगन्धरो योग्यो युशघमंप्रकतंकः । कुछाचारः: कुछकरः कुछदैवकरः: कुर्सी
- **Translation**: 

---

### Verse 15 (Sakand Puran 9.8775)
- **Original**: चतुराधमचारोी च्॑ गुहस्थोी दतिथिप्रियः । वजस्थो वनचारी सा बांगग्रस्यांज्रमाधमी
- **Translation**: 

---

### Verse 16 (Sakand Puran 9.8776)
- **Original**: युग, युगन्धर, योग्य) युगधर्मप्रवर्तक, कुलाचार, कुछकर+ कुलदेवकर, कुकी, चतुराभमचारी, एस, अतिथिप्रिय) वनस्प, वनबारी, बानप्रस्धाअम, आअंमी । बडुको ब्रह्माचारी श्वा सिख्रांसूत्री कमण्डछो। फ्रिज़टी ध्यानवान्‌ ध्यानी वरज्िकाक्रमब्रासकुत्‌
- **Translation**: 

---

### Verse 17 (Sakand Puran 9.8777)
- **Original**: दसादिप्रभभो.. ईसो.. देमराशिदिमाफरः । महाप्रस्थानको विप्रो विरागी रागबांनू गृहों #
- **Translation**: 

---

### Verse 18 (Sakand Puran 9.8778)
- **Original**: [ संक्षिप्त स्कन्दपुराण प्रच्णाभः परीतात्मा परिव्ाटू. पुरुषोत्तमः
- **Translation**: 

---

### Verse 19 (Sakand Puran 9.8779)
- **Original**: नसनारायण) नागी। केदारोदारबिग्रह, गज्ञाद्वारतपःसार 5 निधि, मद्दापद्र। पद्माऊरप्रियाजय, पर्ननाम+ परीतात्मा, परिव्ाट्‌
- **Translation**: 

---

### Verse 20 (Sakand Puran 9.8780)
- **Original**: पुरुषोत्तम । परानन्दः पुराणश्र सन्नाह राजविराजकः । चमघस्थआऋपालस्थञ्ऋव तीं नराधिपः
- **Translation**: 

---

