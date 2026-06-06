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

### Verse 1 (Vishnu Puran 0.9041)
- **Original**: 3 सन्‍्तस्सन्तोषमधिकं प्रशमम॑ चण्डमारुता: । प्रसाद निम्नगा याता जायमाने जनार्दने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9042)
- **Original**: 4 लिए पु 160-- अ्रीपराशरजी छोल्के--हे मैत्रेय ! टेखताओंसे इस प्रकार स्तुति की जाती हुई देवकीजीने संसारको रक्षाके कारण भगवान्‌ पुण्डरीकाक्षको गर्भमें धारण किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9043)
- **Original**: तदनन्तर सम्पूर्ण संसाररूप कमलको विकसित करनेके लिये देवकीरूप पूर्व सब्यामें महात्मा अच्युतरूप सूर्यदेवका आविर्भान हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9044)
- **Original**: चन्द्रगाकी चाँदनीके समान भगवान्‌का जन्म दिन सम्पूर्ण जगत्‌्को आह्वादित करनेवाला हुआ और उस दिन सभी दिल्ञाएँ अत्यन्त निर्मल हो गयीं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9045)
- **Original**: श्रीजनार्दनके जन्म लेनेपर सन्तजनोंको परम सन्तोष हुआ, प्रचण्ड वायू शान्त हो गया तथा नदियाँ अत्यन्त स्वच्छ हो गयीं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9046)
- **Original**: के16 सिन्धवो निजशब्देन बाद्यं चक्रुर्मनोहरम्‌। जगुर्गन्‍धर्वपतयो.. ननुतुश्चाप्सरोगणा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9047)
- **Original**: 5 ससृजु: पुष्पवर्षाणि देवा भुव्यत्तरिक्षगा: । जज्वलुश्चाप्नयइशान्ता जायमाने जनार्दने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9048)
- **Original**: 6 मन्दं जगर्जुर्जलदाः पुष्पवृष्टिमुचो द्विज। अर्द्धरात्रेखिलाधारे जायमाने जनादने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9049)
- **Original**: 7 फुल्लेन्दीवरपत्रा्भ चतुर्बाहुमुदीक्ष्य तम्‌। श्रीवत्सवक्षसं॑ जात॑तुष्टावानकदुन्दुभि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9050)
- **Original**: 8 अभिष्टूय च त॑ वाग्भि: प्रसन्नाभिर्महामति: । विज्ञापयापास तदा कंसाद्धीतो ट्विजोत्तम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9051)
- **Original**: 9 वसुदेव उवाच जातो5सि देवदेवेश शब्बुचक्रगदाधरम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9052)
- **Original**: दिव्यरूपपिंदे_ देव प्रसादेनोपसंहर
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9053)
- **Original**: 10 अद्यैव देव कंसो5य॑ कुरुते मम घातनम्‌। अवतीर्ण इति ज्ञात्वा स्वमस्मिन्‍्पम मन्दिरे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9054)
- **Original**: 11 दंवक्‍युवाच यो3नन्तरूपो5खिलबिश्वरूपो गर्भेषपि लछोकान्वपुषा बिभर्त्ति । प्रसीदतामेष. स॒ देबदेवों यो. माययाविष्कृतबालरूप:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9055)
- **Original**: 12 उपसंहर सर्वात्मिन्नूपमेतच्चतुर्भुजम्‌ । जानातु मावतारं ते कंसो5यं दितिजन्मज:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9056)
- **Original**: 13 अऔरीभगवानुवाच स्तुतो5हं यक्त्वया पूर्व पुत्रार्थिन्या तद्द्य ते । सफल देवि सझ्ात॑ जातो5हं यत्तवोदरात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9057)
- **Original**: 14 श्रीपराशर उताच इत्युक्त्वा भगवांस्तृष्णीं वभूख मुनिसत्तम । बसुदेबो5पि ते रात्राबादाय प्रययो बहिः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9058)
- **Original**: 95 मोहिताश्चाभवंस्तत्र रक्षिणो योगनिद्रया। मथुराद्वारपालाश्न॒ ब्रजत्यानकदुन्दुभी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9059)
- **Original**: 16 अ्रीविष्णूपुराण [0 रे समुद्रगण अपने घोषसे मनोहर बाजे बजाने लगे, गन्धर्वराज गान करने छगे और अप्सराएँ नाचने लगीं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9060)
- **Original**: श्रीजनार्दनके प्रकर होनेपर आकाशगामी देवगण पृथिवीपर पुष्प बरसाने लगे तथा शान्त हुए यज्ञाग्रि फिर प्रण्वच्छित हो गये
- **Translation**: 

---

