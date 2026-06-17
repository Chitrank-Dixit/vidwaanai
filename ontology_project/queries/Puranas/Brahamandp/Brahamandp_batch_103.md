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

### Verse 1 (Brahamandp 0.2041)
- **Original**: 8 आदित्यमंडले दृष्टू वा
- **Translation**: 

---

### Verse 2 (Brahamandp 0.2042)
- **Original**: दृष्ट वा चक्र दुुुच्चक्रे:
- **Translation**: 

---

### Verse 3 (Brahamandp 0.2043)
- **Original**: . (..... 6 क्रव्यादा बहवस्ततव।लोचनेनवलोकिता:
- **Translation**: 

---

### Verse 4 (Brahamandp 0.2044)
- **Original**: , मुहुराकाशवाणीक्षि:: पह़षाधिब्ेश्नाषिरे
- **Translation**: 

---

### Verse 5 (Brahamandp 0.2045)
- **Original**: . .. . .
- **Translation**: 

---

### Verse 6 (Brahamandp 0.2046)
- **Original**: ., सबंतो दिक्षु दृश्यंते।केतवस्तु मलीमस्रा::
- **Translation**: 

---

### Verse 7 (Brahamandp 0.2047)
- **Original**: 10 .. घूमायमाना: प्रक्षोभजनका द॑ त्यरक्षप्ताम्‌ । दंत्यस्त्री णां ।चः विभ्रश्ट, अभ्रकाले भूषणसुज: .
- **Translation**: 

---

### Verse 8 (Brahamandp 0.2048)
- **Original**: 11, हाह्देति दूर ऋन्‍्द्र त्य:. प्रयश्रु सम्नरोद्रिषु: । (35 दपं णानां कमंण्ां ज्ञः शवज़ाता खड गसंपुदाम्‌
- **Translation**: 

---

### Verse 9 (Brahamandp 0.2049)
- **Original**: मणीनामंबराणां त्ञ मालिन्यमभवल्मुहु: । ., '... ., सौधेषु चन्द्रशालासु केलिवेश्मसु स॒वेत. .
- **Translation**: 

---

### Verse 10 (Brahamandp 0.2050)
- **Original**: 33 ,, .,
- **Translation**: 

---

### Verse 11 (Brahamandp 0.2051)
- **Original**: भंडांसुर अहकॉर वर्णन] [ 273 अट्ठालकेषु गोष्ठेषु विपंणेषु सभासु च। चतुष्किकास्वलिदेषु प्रग्नीवेषु वलेषु च
- **Translation**: 

---

### Verse 12 (Brahamandp 0.2052)
- **Original**: 14 उस देत्य के पुर में निवास करने बाले लोग अक्राल में ही हृदय के कम्प से संयत हो गये थे
- **Translation**: 

---

### Verse 13 (Brahamandp 0.2053)
- **Original**: ध्वजाओं के आगे रहने वाले कंके-ग्रू श्र-वैंक ओर पक्षो आदित्य मंडल में देख-देखंकर बड़े ऊँचे स्वर से क्रन्दत करने लगे । वहाँ पर बहुत से (क्रव्याद राश्षसत्रें गणं थे जो नैत्रों के द्वारा ।दिखलाई नहीं दिये गये थे ।5-6
- **Translation**: 

---

### Verse 14 (Brahamandp 0.2054)
- **Original**: बार-बार आक़ाण लाणियों:के द्वा रा बोलते; थे ओर सभी ओर दिक्ाओं में केतु बहुत हो मलिन दिखलाई, दे रहे ये,19।, वे सब धूमा- प्रमानः हो: रहे थे; और देश्पों: तथा राक्षसों. के हुदय़ों में; बड़े, भारी क्षोम को उत्पन्न करने वाले-थे । और असमय में हो दंत्यों की स्त्रियों के भूषण और सालाऐ, अ्ष्ट होकर गिर रहे थे; ।31/ हालहा -श्वनि करके अश्रूपात करती हुई. कदत़ की ध्वनि में सत्र, रो रहीं थीं वहाँ, पर. दर्पश-वर्म-ध्वजा- खंग़ ,और्‌,सम्प्रदाऐ एव मणि तथा वस्त्रों में बार-बार. मलिनता ही गयी थी । सौधों में-चन्द्र! णालाओं में ..और , सभी , ओर केलि ,करनें के गूहों में महात््‌ भ्रीषण प्रोष सुनाई दिया , करता भ्रा ।(2:13। क्षट्टालिकाओं में-- गोष्ठों प्रं-“बिपणों में और सभा भव्नत्ों में --चतुष्किकाओं में-अलिन्दों प्रय्योवों में; और वलूों में सर्वत्र महान. अशुभ , एवं, कठोर, घोष सुनाई बेता था ।14
- **Translation**: 

---

### Verse 15 (Brahamandp 0.2055)
- **Original**: 6 5 व ] छा (7
- **Translation**: 

---

### Verse 16 (Brahamandp 0.2056)
- **Original**: ' 'संबतोभंद्रंवासिपु नन्‍्थावर्तेपु बेश्मसु:
- **Translation**: 

---

### Verse 17 (Brahamandp 0.2057)
- **Original**: / विच्छ दकेषु, संक्षुब्धेष्वब रोध्रनपालिषु ् ,हस्तिक्रेषु :च ससर्वेषु-गर्भागारपुटेघषु /च, 15, ;; / 63 00 गोपुरेष, कपाटेष वलभीनां व सीमसु/।
- **Translation**: 

---

### Verse 18 (Brahamandp 0.2058)
- **Original**: कर माएका बातायनेष, कक्ष्यांसू धिष्ण्येष च॑ खेलेषं चे।।16 सर्वत्र द॑ त्यनगरवीसिमिंजनमंडले: । अश्रूयन्त महाघोषा: पंछषा भूत॑भाषिता: 17 शिथिली सर्वत्तों जांतां घीरंपेर्णा भयानेका
- **Translation**: 

---

### Verse 19 (Brahamandp 0.2059)
- **Original**: करटेः कटुकालापेरक्ली कि दिव।कर: । आराविष करोटीतां कोट्यश्चापत्तन्भुवि
- **Translation**: 

---

### Verse 20 (Brahamandp 0.2060)
- **Original**: 274 ) [ ब्रह्माण्ड पुराण अपनन्वेदिमध्येप, बिदवः शोणितांभसाम्‌ । केशौघकाश्च निष्पेतु: सर्वेतो धूमधूसराः
- **Translation**: 

---

